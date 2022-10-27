# Baseline for Event Ingestion

This document and associated checklist is intended to be used as a high-level self assesment to determine coverage quality of an operational SIEM environment for a typical organisation.

## Service Model Context

Most organisations are strategically migrating services not unique to their specific business to shared common service models as below. This typically results in the **Identity, Credential and Access Management** and **Data** relevant observables having the greatest value.

![Service Models](../images/servicemodels.png)

The above diagram should be used as a reference when determining what systems it is relevant to capture logs from (i.e. if using IaaS, the service provider logs could be collected in bulk, while if On-Prem then logs would need to be captured from hypervisors, physical servers, storage and physical security).

## Detection Observables

The below queries are intended to be completed from a library of [STIX 2.1 Cyber Observable Objects](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html). The list of observables below has been ordered based on feasibility of comprehensive ingestion of all relevant activities external to an organisation.

1. [IPv4Address](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.IPv4Address), [IPv6Address](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.IPv6Address)
2. [UserAccount](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.UserAccount), [EmailAddress](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.EmailAddress)
3. [DomainName](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.DomainName), [URL](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.URL)
4. [EmailMessage](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.EmailMessage) (date, subject, from, to most relevant)
5. [File](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.File) (SHA256 hash most relevant)

## Detection Assets

The below is a high level summary of assets from which log information should typically be collected from / about. Subsequent queries will refer to these assets.

- **Endpoints** - Devices that users access organisational resources from
- **Servers** - Hypervisors, Servers, Container Platforms
- **Users** - Identity Services (On Premise and SaaS), Application access
- **Mailboxes** - Email mailboxes and associated inbound/outbound flows
- **Network Firewalls (Firewalls)** - Network egress and internal network control points
- **Web Application Firewalls (WAFs)** - Network ingress control points

## Detection Checklist

To validate the below checklist, calculate the percentage coverage of assets (e.g. 8 / 10 Endpoints == 80% coverage) where the below queries are able to be undertaken by the organisations security analysts for a given log retention window (normally 12 months).

- [ ] **Endpoints** - Query a `IPv4Address`, `IPv6Address`, `DomainName` or `URL` across all outbound network traffic.
  - E.g. [Defender Network Protection](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/network-protection?view=o365-worldwide), [Defender Web Protection](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/web-protection-overview?view=o365-worldwide)
- [ ] Query an `IPv4Address`, `IPv6Address` or `DomainName` across all inbound/outbound network traffic.
  - [ ] **Servers** - e.g. [Defender Network Protection](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/network-protection?view=o365-worldwide)
  - [ ] **Firewalls** - e.g. [Sentinel 3rd party connectors](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions)
- [ ] **WAFs** - Query an `IPv4Address` or `IPv6Address` across all inbound network traffic.
- [ ] **Mailboxes** Email events and URL / attachment analysis
  - [ ] Query a `DomainName` or `EmailAddress` across all senders/recipients.
  - [ ] Query a `Subject (EmailMessage)` across all email.
  - [ ] Query a `DomainName` or `URL` across all links inside emails.
  - [ ] Query a `SHA256 Hash (File)` across all attachments inside emails.
- [ ] more to come!

## Detection Analytics

Once the above is validated, an organisation should review its capability to schedule regular detection queries across their environment to detect suspicious behaviour based on threat intelligence feeds, as well as deviations from baseline expected behaviour. A simple example would be determining the subset of users that are allowed to use legacy authentication protocols (NTLM, LDAP, HTTP Basic Auth), and alerting security analysts whenever a user outside of that list attempts to sign in with a legacy authentication protocol.
