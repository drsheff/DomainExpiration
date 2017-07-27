#!/usr/bin/env python3

# Script for Domain Check Expiration
import datetime
import whois
import sys

def difference(domainN):
    domainN = whois.whois(sys.argv[1])
    domainD = domainN.expiration_date
    currentD = datetime.datetime.now()
    return (domainD - currentD).days

print(difference(sys.argv[1]))