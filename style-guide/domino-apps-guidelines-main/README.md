# Domino Apps Guidelines

A starter kit for building Domino applications with Cursor, including frontend code examples, API documentation, and design system rules.

## Quick Start

### 1. Download Frontend Code

Run the script to populate `example_domino_frontend_code/` with the latest frontend code:

```bash
./grab_front_end_code.sh
```

This clones the repository (without git history) into `example_domino_frontend_code/`.

> **Note:** The `example_domino_frontend_code/` folder is gitignored and won't be tracked.

### 2. Copy to Your Cursor Project

#### Option A: Using Terminal

Copy all necessary files to your project:

```bash
cp -r example_domino_frontend_code/* /path/to/your/cursor/project/ && \
cp -r .cursor /path/to/your/cursor/project/ && \
cp .gitignore domino-logo.svg swagger.json governance_swagger.json /path/to/your/cursor/project/
```

#### Option B: Using macOS Finder

1. Open this folder in Finder
2. Press **`Cmd + Shift + .`** to show hidden files (the `.cursor` and `.gitignore` will appear)
3. Select and copy all the files you need to your project folder
4. Press **`Cmd + Shift + .`** again to hide hidden files when done

> **Tip:** Hidden files appear slightly dimmed in Finder when visible.


## Cursor Rules Setup

The `.cursor/rules/` folder contains two rule files:

| Rule | Auto-Applied | Description |
|------|--------------|-------------|
| `how-to-build-domino-apps.mdc` | ✅ Yes | Best practices, API guidelines, and technical constraints |
| `usability_design_principles.mdc` | ❌ No | Design system guidelines, UX principles, and component patterns |

### Applying the Usability Design Principles

The `usability_design_principles.mdc` rule is **not auto-applied** and must be manually included when you want Cursor to follow UX/design guidelines.

**To apply it in a conversation:**

1. In Cursor's chat or composer, type `@` to open the mention picker
2. Select **Files & folders**
3. Navigate to `.cursor/rules/usability_design_principles.mdc`
4. The rule will be included in that conversation's context

**Examples:**

```
@.cursor/rules/usability_design_principles.mdc

Review this component for UX issues
```

```
@.cursor/rules/usability_design_principles.mdc

Build a settings page with a form for user preferences
```

This tells Cursor to follow Domino's design system (button hierarchy, typography, spacing, error handling, etc.) whether you're building new UI, reviewing existing code, or asking for improvements.

## API Reference

- **[swagger.json](swagger.json)** - Main API documentation
- **[governance_swagger.json](governance_swagger.json)** - Governance API documentation
