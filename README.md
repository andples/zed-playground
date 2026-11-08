# Zed playground

One small project per language, for checking that the Zed setup in
[dotfiles](https://github.com/andples/dotfiles) works. Open this folder in Zed and go through
the checklist. Keys are for vim normal mode.

## Checklist

| Language | Open | Try |
|---|---|---|
| Python | `python/stats.py` | hover types (ty), save reorders imports (ruff), `space t` on a test in `test_stats.py` |
| OCaml | `ocaml/lib/shapes.ml` | inferred types inline, `space R` → *OCaml: dune test* |
| Rust | `rust/src/main.rs` | clippy warning on save, ▶ next to `main` and the test |
| C++ | `cpp/main.cpp` | clangd errors and completion, `space R` → *C++: compile & run file* |
| LaTeX | `latex/paper.tex` | save builds the PDF, `space p` opens Skim at the cursor, Cmd-Shift-click jumps back |
| Typst | `typst/notes.typ` | save writes `notes.pdf`, `space p` opens it |
| Markdown | this file | `space p` shows the preview beside it |

## Git

Edit any file and look at the gutter. Then:

- `space g g` git panel: stage, commit, push
- `]c` / `[c` next/previous change, `space g s` stage it, `space g r` undo it
- `space g l` blame on the current line, `space g b` switch branch

## Projects

- `space o` recent projects (fuzzy)
- `space O` open any folder, with Zed's own path picker instead of the macOS dialog
- `space z` jump to a folder you've visited before (zoxide)

```python
def greet(name: str) -> str:
    return f"hello {name}"
```

$$e^{i\pi} + 1 = 0$$
