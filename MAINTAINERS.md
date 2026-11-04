# Maintainer notes

## Publishing to ClawHub

Use a clean checkout of the reviewed commit, with all host manifest versions
synchronized. Publish under the ClawHub `kinprove` owner using an account with
access to that owner. The `@kinprove/` package scope must match it.

```sh
npx --yes clawhub@0.23.3 package validate . --out ../clawhub-validation --json
npx --yes clawhub@0.23.3 package publish . --family code-plugin --owner kinprove --dry-run --json
```

Check that the dry-run reports `code-plugin`, the intended version and the exact
reviewed commit before making a separately authorized live publication. Keep
`--family code-plugin`: Claude manifests coexist in this repository, so automatic
family detection can choose a Claude bundle instead of the native OpenClaw package.
The npm artifact deliberately includes native OpenClaw code and the complete
skill/resources/license tree, not the other hosts' adapters or development files.

A successful dry-run is not a public release. Authenticate securely, publish the
same clean commit with the same flags (without `--dry-run`), and verify its
ClawHub publication/security-check status before announcing availability. Do not
publish to npm merely because this package uses an npm-style scoped name.

## Reproducible installs and audits

To make a direct Hermes repository install reproducible, add
`--ref <full-commit-sha>` to the install command. Public catalog inclusion does not
mean a package is maintained by the host or has received a full security audit.

The native adapters expose bundled instructions, not automatic access to your
DNA accounts or records. They do not make service calls, install an MCP server,
store credentials, send telemetry, or start background jobs. Individual recipes
can describe optional services and commands; executing those still requires the
host's appropriate tools, permissions and any service-specific credentials.
