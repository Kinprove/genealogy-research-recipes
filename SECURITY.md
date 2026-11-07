# Security policy

## Report a security or privacy problem

Email [hola@kinprove.io](mailto:hola@kinprove.io) with the subject
`genealogy-research-recipes security`. Please report privately before opening a
public issue or pull request that reveals the problem.

Include the affected version or commit, file and passage or command, what could
go wrong, and a minimal example using invented or redacted data. Do not send raw
DNA files, private family photographs, account credentials, or identifying details
of living people. We can arrange any necessary follow-up privately.

We aim to acknowledge reports within **7 calendar days** and provide an initial
assessment or status update within **14 calendar days**. These are targets, not
guaranteed response or fix times. If you have no reply after 7 days, please resend
to the same address. We will coordinate a correction and public disclosure with
the reporter; a fix date depends on the problem and any upstream dependency.

## Scope

Reports are welcome for all parts of this repository and its distributed package:

- Recipes, routing instructions and source links that could expose private data,
  bypass consent, send a user to a malicious destination, or instruct an unsafe
  action. A privacy defect in prose is in scope even without executable code.
- The bundled Beider name lookup script and resources.
- Native host adapters, manifests, installation and packaging.
- CI workflows and the release process, including exposed credentials or tampered
  distribution artifacts.

The adapters register bundled instructions; they do not themselves access DNA
accounts or transfer research data. Recipes can describe outbound actions carried
out through the host's tools. Those steps still need the skill's privacy gate and
the relevant person's authorization. A missing gate is reportable; the presence
of a general privacy rule does not excuse an unsafe recipe step.

Fixes are made on `main` and included in the next applicable release. Please
include older affected versions in a report too; separate backports are not
promised. A problem in a third-party host or service should also be reported to
its owner. Unsafe instructions or links in this package remain in scope here.

For ordinary factual corrections and installation failures without sensitive
details, use the [public issue templates](https://github.com/Kinprove/genealogy-research-recipes/issues/new/choose).
