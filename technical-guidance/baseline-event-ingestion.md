# Baseline for Event Ingestion

This document and associated checklist is intended to be used as a high-level self assesment to determine coverage quality of an operational SIEM environment for a typical organisation.

## Service Model Context

Most organisations are strategically migrating services not unique to their specific business to shared common service models as below. This typically results in the **Identity, Credential and Access Management** and **Data** relevant observables having the greatest value.

![Service Models](../images/servicemodels.png)

The above diagram should be used as a reference to determine which systems/services are relevant for capturing security logs (i.e. if utilising IaaS, the service provider should facilitate the collection of security logs in bulk, while On-Premise infrastructure would require additional resoruces to capture security logs from hypervisors, physical servers, storage and physical security).

## Detection Observables

Referencing the [STIX 2.1 Cyber Observable Objects](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v2 ) library, the below observables are intended to represent an organisation detection scope of potential threat indicators. The observables objects are ordered based on feasibility of ingestion of all relevant activities external to an organisation.

1. [IPv4Address](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.IPv4Address), [IPv6Address](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.IPv6Address)
2. [UserAccount](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.UserAccount), [EmailAddress](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.EmailAddress)
3. [DomainName](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.DomainName), [URL](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.URL)
4. [EmailMessage](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.EmailMessage) (date, subject, from, to most relevant)
5. [File](https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.observables.html#stix2.v21.observables.File) (SHA256 hash most relevant)

> Futher information of the purpose of STIX 2.1 and the observable objects can be found [here](https://oasis-open.github.io/cti-documentation/stix/intro.html).

## Detection Assets

The below is a high level summary of assets and services from where security logs should typically be collected. Subsequent detection queries will refer to these assets.

- **Endpoints** - Devices that users access organisational resources from
- **Servers** - Hypervisors, Servers, Container Platforms
- **Users** - Identity Services (On Premise and SaaS), Application access
- **Mailboxes** - Email mailboxes and associated inbound/outbound flows
- **Network Firewalls (Firewalls)** - Network egress and internal network control points
- **Web Application Firewalls (WAFs)** - Network ingress control points

# Detection Checklist

The below checklist should be undertaken by the organisations security team to calculate the percentage coverage of assets (e.g. 8 / 10 Endpoints == 80% coverage) for a given log retention window (normally 12 months).

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

Once the above checklist is validated, an organisation should schedule regular security exercises to detect for suspicious behaviour based on indicators collected from threat intelligence soruces and to detect for deviations against known behaviour baselines. A simple example would be to determine a subset of users that are allowed to use legacy authentication protocols (NTLM, LDAP, HTTP Basic Auth), and alerting security analysts whenever a user outside of that list attempts to sign in with a legacy authentication protocol.
