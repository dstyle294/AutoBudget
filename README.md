# Budget Automation

Turns Chase CSV exports (credit card + bank) into categorized, flagged
transactions in a local database, synced to your existing Google Sheet.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export BUDGET_SHEET_ID=your_google_sheet_id  # from the sheet's URL
```

For Google Sheets sync, see the setup steps at the top of `src/sheets_sync.py`
(service account + sharing the sheet with it).

## Usage

1. Export CSVs from Chase (credit card and/or bank account) into `data/raw/`.
2. Run the pipeline:
   ```bash
   python -m src.main data/raw/*.csv
   ```
3. Review anything flagged (printed at the end of the run, also queryable
   in `data/budget.db` with `needs_review=1`).
4. Generate charts:
   ```bash
   python -c "from src import storage, visualize; c = storage.get_connection(); visualize.spending_by_category(c); visualize.monthly_trend(c)"
   ```
5. Sync to your Sheet:
   ```bash
   python -m src.sheets_sync sync
   ```

## Editing categories

Edit `config/categories.yaml` — add/remove categories, add keywords as you
notice merchants that should route to a rule instead of the LLM fallback.
Flag thresholds live in the same file.

## Project layout

```
config/categories.yaml   - your categories, keyword rules, flag thresholds
src/normalize.py         - CSV -> common transaction schema
src/storage.py           - SQLite storage + dedup
src/categorize.py        - rule-based + LLM fallback categorization
src/flags.py             - flagging logic (large, new, duplicate, low-confidence)
src/visualize.py         - local charts + summary tables
src/sheets_sync.py       - push to Google Sheets
src/main.py              - orchestrates the full pipeline
data/raw/                - drop CSV exports here
data/processed/          - generated charts land here
data/budget.db           - SQLite source of truth (gitignored)
```
