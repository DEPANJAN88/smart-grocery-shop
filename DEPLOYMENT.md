# Deployment Guide — Commercial Distribution

## System Requirements

| Requirement | Minimum |
|-------------|---------|
| OS | Windows 10+, Ubuntu 20+, macOS 11+ |
| Python | 3.9 or higher |
| RAM | 2 GB |
| Disk | 500 MB free |
| Network | Not required after install |

## Customer Installation (Windows)

1. Copy the entire `grocery_shop` folder to the customer's PC
2. Run `install.bat` (one time)
3. Run `run_production.bat` daily to start the shop
4. Browser opens automatically at `http://127.0.0.1:5000`
5. Complete the **Setup Wizard** (shop name + owner login)
6. Enter **license key** in Settings (or use 30-day trial)

## Customer Installation (Linux/Mac)

```bash
cd grocery_shop
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -c "from database import init_db; init_db()"
python run_production.py
```

## LAN Access (Shop Tablet/Phone)

Edit `.env`:
```
HOST=0.0.0.0
PORT=5000
```

Restart the server. Other devices on the same Wi-Fi can access:
`http://<shop-pc-ip>:5000`

**Security:** Only use LAN mode on trusted shop networks. Keep firewall enabled.

## License Key Management (Vendor)

Generate keys for paying customers:

```bash
venv\Scripts\python.exe tools\generate_license.py RAMP
# Output: GSM-RAMP-XXXX-XXXX
```

**Before distribution:** Change `LICENSE_SECRET` in `.env` to a unique vendor secret. Never share this secret.

## User Roles

| Role | Access |
|------|--------|
| **Owner** | Full access — analytics, reports, backup, settings, user management |
| **Staff** | Sales, payments, customers, products — no reports/settings |

## Backup Strategy

| Frequency | Action |
|-----------|--------|
| Daily | Reports → Create Backup (or auto on startup) |
| Weekly | Copy `data/backups/` to USB |
| Monthly | Copy entire `data/` folder offsite |

Database file: `data/grocery_shop.db`

## Log Files

Production logs: `data/logs/app.log` (rotates at 2 MB, keeps 5 files)

## Security Checklist

- [ ] Change `LICENSE_SECRET` in `.env` before shipping
- [ ] Each installation auto-generates unique `SECRET_KEY` in `data/.secret_key`
- [ ] Use strong owner password (6+ characters)
- [ ] Create staff accounts instead of sharing owner login
- [ ] Bind to `127.0.0.1` unless LAN access is needed
- [ ] Take daily backups

## Updating to New Version

1. Stop the running server (Ctrl+C)
2. Backup `data/grocery_shop.db`
3. Replace application files (keep `data/` folder)
4. Run `install.bat`
5. Restart `run_production.bat`

Database migrations run automatically on startup.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Port in use | Change `PORT=5001` in `.env` |
| Trial expired | Enter license in Settings or `/activate-license` |
| Forgot password | Restore DB backup or contact vendor |
| Blank page styles | Static CSS is bundled — clear browser cache |

## Commercial Packaging Checklist

- [ ] Custom `LICENSE_SECRET` per vendor
- [ ] Branded shop name in setup wizard
- [ ] License keys generated per customer
- [ ] Installation tested on clean Windows PC
- [ ] Backup/restore procedure documented for customer
- [ ] Support contact included in README