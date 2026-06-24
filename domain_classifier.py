#!/usr/bin/env python3
"""
Phishing Domain OSINT Analyzer

Analyzes suspicious domains for indicators of phishing/malicious activity.
Checks: domain age, WHOIS data, DNS records, SSL certificates, reputation.

Usage:
    python domain_classifier.py --domain suspiciousdomain.com --output report.json
    python domain_classifier.py --input domains.txt --threshold 0.70

Author: Bipin Shrestha
License: MIT
"""

import json
import argparse
import socket
import ssl
import datetime
from urllib.parse import urlparse
import subprocess
import sys

class PhishingDomainAnalyzer:
    """Analyzes domains for phishing indicators."""
    
    # Phishing risk indicators
    PHISHING_INDICATORS = {
        "domain_age_new": {
            "factor": 0.25,
            "description": "Domain registered less than 30 days ago"
        },
        "domain_age_suspicious": {
            "factor": 0.15,
            "description": "Domain registered less than 90 days ago"
        },
        "suspicious_tld": {
            "factor": 0.20,
            "description": "Uses uncommon TLD (.tk, .ml, .ga, .cf)"
        },
        "homograph_attack": {
            "factor": 0.30,
            "description": "Domain resembles legitimate brand (instagram.net vs instagram.com)"
        },
        "no_https": {
            "factor": 0.25,
            "description": "Website does not use HTTPS"
        },
        "self_signed_cert": {
            "factor": 0.25,
            "description": "SSL certificate is self-signed"
        },
        "certificate_mismatch": {
            "factor": 0.20,
            "description": "Certificate domain doesn't match website domain"
        },
        "no_whois_info": {
            "factor": 0.15,
            "description": "WHOIS information is redacted/private"
        },
        "suspicious_registrar": {
            "factor": 0.15,
            "description": "Registered with privacy-focused registrar"
        },
        "parked_domain": {
            "factor": 0.20,
            "description": "Domain is parked (generic landing page)"
        },
        "short_domain_age": {
            "factor": 0.10,
            "description": "Domain has short history"
        }
    }

    def __init__(self):
        self.analysis_results = {}
        self.risk_score = 0
        self.detected_indicators = []

    def analyze_domain(self, domain):
        """
        Analyze a domain for phishing indicators.
        
        Args:
            domain (str): Domain to analyze (e.g., suspiciousdomain.com)
            
        Returns:
            dict: Analysis results
        """
        self.domain = domain
        self.analysis_results = {
            "domain": domain,
            "timestamp": datetime.datetime.now().isoformat(),
            "indicators": [],
            "risk_score": 0,
            "risk_level": "UNKNOWN",
            "recommendations": []
        }

        print(f"[*] Analyzing domain: {domain}")
        
        # Check domain format
        self._validate_domain()
        
        # Check domain age
        self._check_domain_age()
        
        # Check TLD
        self._check_tld()
        
        # Check for homograph attacks
        self._check_homograph_attack()
        
        # Check HTTPS/SSL
        self._check_https()
        
        # Check WHOIS
        self._check_whois()
        
        # Calculate risk score
        self._calculate_risk_score()
        
        # Generate recommendations
        self._generate_recommendations()
        
        return self.analysis_results

    def _validate_domain(self):
        """Validate domain format."""
        print("[*] Validating domain format...")
        
        # Check if domain has at least one dot
        if "." not in self.domain:
            self.analysis_results["error"] = "Invalid domain format"
            return False
        
        # Try to resolve domain
        try:
            ip_address = socket.gethostbyname(self.domain)
            self.analysis_results["ip_address"] = ip_address
            print(f"    [+] Domain resolves to IP: {ip_address}")
        except socket.gaierror:
            self.analysis_results["indicators"].append({
                "indicator": "dns_resolution_failed",
                "severity": "MEDIUM",
                "description": "Domain does not resolve to any IP address"
            })
            print(f"    [!] Warning: Domain does not resolve")
        
        return True

    def _check_domain_age(self):
        """Check domain registration age."""
        print("[*] Checking domain age...")
        
        # This would require WHOIS API (not available without external service)
        # For demo, we'll check with a simple command-line whois lookup
        
        try:
            result = subprocess.run(
                ["whois", self.domain],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            whois_data = result.stdout
            
            # Look for creation date
            if "Creation Date:" in whois_data or "created:" in whois_data.lower():
                print("    [+] Domain has creation date (likely not brand new)")
            elif "No Found" in whois_data or "Not found" in whois_data:
                self.analysis_results["indicators"].append({
                    "indicator": "domain_age_new",
                    "severity": "HIGH",
                    "risk_factor": 0.25,
                    "description": "Domain appears to be recently registered"
                })
                print("    [!] Alert: Domain appears very new")
            
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print("    [*] WHOIS lookup not available (install whois tool)")

    def _check_tld(self):
        """Check for suspicious TLDs."""
        print("[*] Checking TLD...")
        
        suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.top', '.bid', 
                          '.site', '.trade', '.science', '.review']
        
        tld = "." + self.domain.split(".")[-1]
        
        if tld.lower() in suspicious_tlds:
            self.analysis_results["indicators"].append({
                "indicator": "suspicious_tld",
                "severity": "MEDIUM",
                "risk_factor": 0.20,
                "description": f"Uses suspicious TLD: {tld}"
            })
            print(f"    [!] Alert: Suspicious TLD detected: {tld}")
        else:
            print(f"    [+] TLD {tld} is standard")

    def _check_homograph_attack(self):
        """Check for homograph/typosquatting indicators."""
        print("[*] Checking for homograph attacks...")
        
        # Common legitimate domains to check against
        legitimate_brands = {
            "instagram": ["instagram.com"],
            "facebook": ["facebook.com"],
            "google": ["google.com"],
            "amazon": ["amazon.com"],
            "apple": ["apple.com"],
            "microsoft": ["microsoft.com"],
            "twitter": ["twitter.com"],
            "linkedin": ["linkedin.com"],
            "gmail": ["gmail.com"],
            "paypal": ["paypal.com"]
        }
        
        domain_lower = self.domain.lower()
        
        for brand, legit_domains in legitimate_brands.items():
            if brand in domain_lower and self.domain not in legit_domains:
                self.analysis_results["indicators"].append({
                    "indicator": "homograph_attack",
                    "severity": "CRITICAL",
                    "risk_factor": 0.30,
                    "description": f"Domain resembles legitimate brand: {brand}",
                    "legitimate_domains": legit_domains,
                    "suspicious_domain": self.domain
                })
                print(f"    [!] ALERT: Possible homograph attack on '{brand}'")
                print(f"       Suspicious: {self.domain}")
                print(f"       Legitimate: {legit_domains}")

    def _check_https(self):
        """Check for HTTPS and SSL certificate."""
        print("[*] Checking HTTPS/SSL...")
        
        try:
            # Try to connect with SSL
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    print("    [+] HTTPS connection successful")
                    
                    # Check certificate validity
                    if cert:
                        subject = dict(x[0] for x in cert.get('subject', ()))
                        cn = subject.get('commonName', '')
                        
                        if cn != self.domain:
                            self.analysis_results["indicators"].append({
                                "indicator": "certificate_mismatch",
                                "severity": "MEDIUM",
                                "risk_factor": 0.20,
                                "description": f"Certificate CN ({cn}) doesn't match domain"
                            })
                            print(f"    [!] Warning: Certificate mismatch (CN: {cn})")
                    
        except ssl.SSLError as e:
            self.analysis_results["indicators"].append({
                "indicator": "ssl_error",
                "severity": "HIGH",
                "risk_factor": 0.25,
                "description": f"SSL error: {str(e)}"
            })
            print(f"    [!] Alert: SSL certificate issue: {e}")
        
        except socket.timeout:
            self.analysis_results["indicators"].append({
                "indicator": "https_unavailable",
                "severity": "HIGH",
                "risk_factor": 0.25,
                "description": "HTTPS connection timeout or not available"
            })
            print(f"    [!] Alert: HTTPS not available on port 443")
        
        except Exception as e:
            print(f"    [*] Could not verify HTTPS: {e}")

    def _check_whois(self):
        """Check WHOIS information."""
        print("[*] Checking WHOIS information...")
        
        # Note: Would require WHOIS API for production
        # This is a placeholder for demonstration
        print("    [*] WHOIS check requires API access")

    def _calculate_risk_score(self):
        """Calculate overall risk score (0-100)."""
        print("[*] Calculating risk score...")
        
        total_risk = 0
        
        for indicator in self.analysis_results["indicators"]:
            if "risk_factor" in indicator:
                total_risk += indicator["risk_factor"]
        
        # Cap at 1.0 and convert to percentage
        risk_percentage = min(100, total_risk * 100)
        
        self.analysis_results["risk_score"] = risk_percentage
        
        # Determine risk level
        if risk_percentage >= 80:
            self.analysis_results["risk_level"] = "CRITICAL"
        elif risk_percentage >= 60:
            self.analysis_results["risk_level"] = "HIGH"
        elif risk_percentage >= 40:
            self.analysis_results["risk_level"] = "MEDIUM"
        elif risk_percentage >= 20:
            self.analysis_results["risk_level"] = "LOW"
        else:
            self.analysis_results["risk_level"] = "MINIMAL"
        
        print(f"    [+] Risk Score: {risk_percentage:.1f}/100")
        print(f"    [+] Risk Level: {self.analysis_results['risk_level']}")

    def _generate_recommendations(self):
        """Generate recommendations based on findings."""
        print("[*] Generating recommendations...")
        
        risk_level = self.analysis_results["risk_level"]
        
        if risk_level == "CRITICAL":
            self.analysis_results["recommendations"].append(
                "BLOCK this domain immediately"
            )
            self.analysis_results["recommendations"].append(
                "Report to phishing database (PhishTank, URLhaus)"
            )
            self.analysis_results["recommendations"].append(
                "Investigate users who visited this domain"
            )
            self.analysis_results["recommendations"].append(
                "Alert email users to report emails linking to this domain"
            )
        
        elif risk_level == "HIGH":
            self.analysis_results["recommendations"].append(
                "Add to email filtering blacklist"
            )
            self.analysis_results["recommendations"].append(
                "Monitor for emails linking to this domain"
            )
            self.analysis_results["recommendations"].append(
                "Verify legitimacy before allowing access"
            )
        
        elif risk_level == "MEDIUM":
            self.analysis_results["recommendations"].append(
                "Apply enhanced monitoring"
            )
            self.analysis_results["recommendations"].append(
                "Verify SSL certificate validity"
            )
            self.analysis_results["recommendations"].append(
                "Check against threat intelligence feeds"
            )
        
        # General recommendations
        self.analysis_results["recommendations"].append(
            "Verify domain against threat intelligence (VirusTotal, URLhaus)"
        )
        self.analysis_results["recommendations"].append(
            "Educate users about phishing indicators"
        )

    def generate_report(self, format="json"):
        """Generate analysis report."""
        if format == "json":
            return json.dumps(self.analysis_results, indent=2)
        
        # Text format
        report = []
        report.append("=" * 80)
        report.append("PHISHING DOMAIN ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"Domain: {self.analysis_results['domain']}")
        report.append(f"Timestamp: {self.analysis_results['timestamp']}")
        report.append(f"Risk Score: {self.analysis_results['risk_score']:.1f}/100")
        report.append(f"Risk Level: {self.analysis_results['risk_level']}")
        report.append("")
        
        report.append("INDICATORS DETECTED")
        report.append("-" * 80)
        if self.analysis_results["indicators"]:
            for i, ind in enumerate(self.analysis_results["indicators"], 1):
                report.append(f"{i}. {ind.get('indicator', 'Unknown')}")
                report.append(f"   Severity: {ind.get('severity', 'N/A')}")
                report.append(f"   Description: {ind.get('description', 'N/A')}")
                report.append("")
        else:
            report.append("No suspicious indicators detected.")
            report.append("")
        
        report.append("RECOMMENDATIONS")
        report.append("-" * 80)
        for i, rec in enumerate(self.analysis_results["recommendations"], 1):
            report.append(f"{i}. {rec}")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)


def main(args):
    """Main function."""
    
    analyzer = PhishingDomainAnalyzer()
    
    # Single domain analysis
    if args.domain:
        print(f"[+] Analyzing single domain: {args.domain}")
        result = analyzer.analyze_domain(args.domain)
        
        # Output results
        if args.output:
            output_format = "json" if args.output.endswith(".json") else "text"
            report = analyzer.generate_report(format=output_format)
            
            with open(args.output, 'w') as f:
                f.write(report)
            
            print(f"\n[+] Report saved to {args.output}")
        
        # Print summary
        print("\n" + analyzer.generate_report(format="text"))
    
    # Batch analysis from file
    elif args.input:
        print(f"[+] Batch analyzing domains from {args.input}")
        
        results = []
        try:
            with open(args.input, 'r') as f:
                domains = f.read().strip().split('\n')
            
            for domain in domains:
                domain = domain.strip()
                if domain:
                    print(f"\n[*] Analyzing: {domain}")
                    result = analyzer.analyze_domain(domain)
                    results.append(result)
            
            # Save batch results
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(results, f, indent=2)
                print(f"\n[+] Batch results saved to {args.output}")
            
            # Print summary
            high_risk = [r for r in results if r['risk_level'] in ['CRITICAL', 'HIGH']]
            print(f"\n[+] Summary: {len(high_risk)} high-risk domains detected")
        
        except FileNotFoundError:
            print(f"[!] Error: File {args.input} not found")
            sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze domains for phishing indicators"
    )
    
    parser.add_argument(
        "--domain",
        help="Single domain to analyze"
    )
    parser.add_argument(
        "--input",
        help="File with list of domains (one per line)"
    )
    parser.add_argument(
        "--output",
        help="Output report file (JSON or TXT)"
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.70,
        help="Risk threshold for flagging (0.0-1.0, default: 0.70)"
    )
    
    args = parser.parse_args()
    
    if not args.domain and not args.input:
        parser.print_help()
        sys.exit(1)
    
    main(args)
