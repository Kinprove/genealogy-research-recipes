---
id: "us-wwi-va-master-index-benefits"
title: "Decode a World War I VA Master Index card and trace its benefit files"
summary: "Decode claim, bonus, insurance and rehabilitation numbers on a World War I VA Master Index card, then route the surviving records by number and custodian."
kind: "records"
scope: {"platforms": [], "tasks": ["Deceased Veterans Claim File", "World War Adjusted Compensation Act", "War Risk Term Insurance"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "US-WWI-VA-MASTER-INDEX-BENEFITS-01", "text": "Keep each prefix with its own number."}]
handoff: ["us-20th-century-military-service-reconstruction"]
checked: null
checked_basis: null
capabilities: {"browse": ["FamilySearch collection descriptions and card images", "National Archives finding aids and disposition schedules", "historical statutes"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool", "request"], "contact": []}
router: {"section": "Records by country and region", "group": "United States: military, land, courts and law", "order": 297}
---

# Decode a World War I VA Master Index card and trace its benefit files

## Find the card and read the code key

**Privacy gate:** <!-- privacy-gate: third-party-tool --> FamilySearch receives the veteran’s service name in the card search.

Search the veteran’s service name in FamilySearch’s *United States, Veterans Administration Master Index, 1917–1940*. Open the card image and copy its locator and both sides when available. [S2 @2026-11-22]

According to the presenter, consult the code key before reading the card’s prefixes. [S1†] Use the National Archives’ *VA Master Index Codes* for the definitions. [S3]

Keep each prefix with its own number. Preserve additions, blank fields and separate dates as written. Read `C` as the benefit claim number and `XC` as the claim marked after the veteran’s death. If the card dates the addition of `X`, record that as the annotation date and use the separately labelled death date for the death entry. The `X` also leaves the date of claim closure unresolved. [S3] [S4]

Read `K` as U.S. Government Life Insurance, which could follow conversion from `T` or a direct application. Read `T` as World War I War Risk term insurance and `R` as the World War I rehabilitation field. Read `A` as an adjusted-compensation number and `CT` as the service department’s bonus certificate number. Preserve `UA` as written and check the payment papers for an unpaid balance. [S3]

## Trace the numbered XC claim

**Privacy gate:** <!-- privacy-gate: request --> St. Louis archives staff receive the requester’s contact details and the deceased veteran’s claim number and identifying details. A claim file may also concern a living beneficiary and disclose health or dependency information. Apply the record-request rules before sending.

Use the full XC number in a request to the National Archives at St. Louis for its Deceased Veterans Claim Files in Record Group 15. Give the full service name and any requested service number and vital or service dates you have. If the case remained open into or after 1955, or St. Louis finds no file in its accessions, verify whether the VA retains custody and follow the [VA claim-file route](us-20th-century-military-service-reconstruction.md#request-records-that-were-never-part-of-the-ompf). [S4 @2026-11-22] [S5 @2026-11-22]

## Read the federal bonus papers

Separate adjusted-service credit, certificate face value and actual disbursement. Under the 1924 act, check qualifying service after April 5, 1917 and before July 1, 1919, in excess of 60 days. Use the exclusions in section 202 and count home service first toward the 60 days when service was mixed. Calculate credit at $1 per day of home service and $1.25 per day overseas, with a $500 cap for veterans without overseas service and $625 for veterans with any overseas service. Keep the cap on the credit side of the worksheet. [S6]

For a credit of $50 or less, look for adjusted-service pay after application, payable no earlier than March 1, 1925. For a larger credit, look for the certificate and its actual issue date. The original act specified payment 20 years after the certificate date. For earlier death, look for payment to the named beneficiary or to the veteran’s estate if there was no surviving designated beneficiary. Check for a surrender and settlement under the 1936 act before assigning a payment date, and record the recipient the papers actually name. [S6] [S7]

## Account for separately disposed series

For World War I Bonus Finance Cards from 1924–1940, check schedule `NC1-015-79-12` for accession `70-A-6324`. The schedule’s cover records destruction at the Washington National Records Center in December 1979. Keep that loss scoped to the accession. Continue tracing the `CT` certificate or the separate `XC` claim when you have those leads. [S8]

For a `T` number, check whether the policy had lapsed without conversion. Schedule `NC-174-000213` authorized immediate disposal of that subset of World War I yearly renewable term folders for 1917–1921. The National Archives’ cover sheet lists disposal as assumed. Keep any `K` policy or numbered claim as a separate lead. [S3] [S9]

## Return the file register

Give one row per card, claim, insurance policy, bonus certificate or finance-card series. Preserve its number, dates and date roles, locator, access outcome and next retrieval action. Use [U.S. military service reconstruction](us-20th-century-military-service-reconstruction.md) for personnel records, state bonuses and other auxiliary series.
