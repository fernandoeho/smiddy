# Workflow: Release

Use this workflow to prepare, validate, and ship a versioned release.

---

## When to Use

- Cutting a version tag for production deployment
- Publishing a package or artifact
- Coordinating a set of merged features into a release branch

## When Not to Use

- Building a feature → use `new-feature.md`
- Fixing a bug → use `bug-fix.md`

---

## Prerequisites

Before starting this workflow:
- All feature and fix branches for this release are merged to `main`
- All spec files for included work are status: Done
- No open blocking issues in recent reviews

---

## Phase Sequence

```
Prepare ──► Validate ──► Document ──► Tag ──► Deploy ──► Verify
```

---

## Step 1 — Prepare

Determine the version number using semantic versioning:
- **MAJOR** — breaking changes to public API or behavior
- **MINOR** — new features, backwards-compatible
- **PATCH** — bug fixes only, backwards-compatible

Check `.smiddy/context/decisions.md` for any versioning policy decisions that override this default.

Create a release branch:
```
release/<version>   e.g. release/1.4.0
```

---

## Step 2 — Validate

Run the full test suite on the release branch. All tests must pass.

If tooling is configured, also run:
- Type checking
- Linting
- Security scanning
- Dependency audit

Do not proceed if any check fails. Failures go back to `main` as bug fixes.

---

## Step 3 — Document

**Changelog:** Compile entries from all merged specs since the last release. Group by:
- Breaking Changes (if any)
- New Features
- Bug Fixes
- Deprecations

**Migration guide:** If there are breaking changes, write a migration guide describing what callers must change.

**Release notes:** A plain-language summary of what is new, what is fixed, and what is removed. Written for users, not developers.

---

## Step 4 — Tag

Create a signed, annotated git tag:
```
v<version>   e.g. v1.4.0
```

Tag message should include the one-paragraph release summary.

---

## Step 5 — Deploy

Follow the deployment procedure for this project (documented in `.smiddy/specs/architecture.md` under Infrastructure, or in a separate runbook).

Record the deployment in `.smiddy/context/decisions.md` if it involves a significant infrastructure change.

---

## Step 6 — Verify

After deployment, verify the release in the target environment:
- Smoke test the primary user flows
- Confirm monitoring shows no error rate spike
- Confirm the version identifier exposed by the system matches the release tag

If post-deploy issues are found, do not roll back automatically — diagnose first. A targeted hotfix via `bug-fix.md` is usually preferable to a full rollback.

---

## Checklist

### Prepare
- [ ] Version number determined
- [ ] Release branch created from `main`

### Validate
- [ ] Full test suite passes
- [ ] Type check passes (if applicable)
- [ ] Lint passes (if applicable)
- [ ] Security scan passes (if applicable)

### Document
- [ ] Changelog updated for all included changes
- [ ] Migration guide written (if breaking changes)
- [ ] Release notes written

### Ship
- [ ] Release branch merged to `main`
- [ ] Annotated tag created
- [ ] Deployment executed
- [ ] Smoke tests pass post-deploy
- [ ] Monitoring confirms no regressions
