# Data collection integration notes

This project currently uses synthetic demonstration data. For real data, use official platform APIs and comply with their terms, privacy rules, rate limits, and consent requirements.

- YouTube: YouTube Data API v3 can provide permitted public video/channel metadata and statistics. Some metrics (such as retention) are generally available only to channel owners through YouTube Analytics API with OAuth authorization.
- Instagram: Instagram Graph API access depends on account type, permissions, review, and approved use cases. Do not scrape private content or bypass access controls.
- Store API credentials in environment variables or Colab Secrets; never commit tokens to GitHub.
- Add provenance columns (platform, collected_at, source_id, permission_scope) to production datasets.
