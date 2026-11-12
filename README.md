# Data-Driven Social Engagement Initiative

A research-oriented social analytics prototype that measures content performance, estimates a weighted virality proxy, analyzes audience comments, compares content variants, recommends content combinations, and visualizes engagement/trend signals.

## Project modules
1. **Content Performance Tracker** – structured post and comment datasets; API integration guidance is in `src/data_collection_notes.md`.
2. **Virality Prediction Engine** – weighted viral coefficient proxy that values shares and saves above likes, plus a Random Forest classifier.
3. **Audience Sentiment Analyzer** – baseline sentiment and relatability tagging for comments.
4. **A/B Testing Framework** – pairwise Mann–Whitney comparisons for formats/hooks/caption lengths.
5. **Engagement Optimization Recommender** – ranks topic/format/hook combinations using historical group metrics.
6. **Growth Visualization Dashboard** – Streamlit interface for engagement, sentiment, viral metrics, and trends.
7. **Trend Forecasting Signals** – exploratory hashtag score time series and visualization.

## Quick start (local)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Google Colab
Open `Social_Engagement_Analytics_Colab.ipynb` in Google Colab. Upload/extract this project ZIP into `/content`, then run the notebook from top to bottom. To expose Streamlit, add an `NGROK_AUTH_TOKEN` secret in Colab and run the final launch cell.

## Data
- `data/social_posts.csv`: 1,200 synthetic post records.
- `data/comments.csv`: 2,200 synthetic comments.
- `data/hashtag_trends.csv`: synthetic hashtag trend scores.

**All bundled data are synthetic and are intended only to demonstrate the pipeline.** Do not report the resulting scores, model performance, sentiment distributions, or recommendations as real-world findings. Replace the data with authorized, properly documented platform data before drawing operational conclusions.

## Method notes and limitations
- Engagement rate = (likes + comments + shares + saves) / reach × 100.
- Viral coefficient proxy = (2 × shares + 2 × saves + comments) / reach. This is a project-defined weighted indicator, not a standardized industry metric or a guarantee of virality.
- The high-viral-potential label is defined using the 80th percentile of the coefficient in this dataset. This is a relative label, not a universal threshold.
- A/B-style tests compare observational groups. They are not causal unless content variants are assigned through a controlled randomized experiment.
- Comment sentiment/relatability is a simple lexicon baseline, not a validated clinical or demographic inference system.
- Hashtag trends are simulated, not live external trend data.
- Use official platform APIs, follow their terms, respect user privacy/consent, and never commit API keys or OAuth tokens.

## Repository layout
```text
Data_Driven_Social_Engagement_Initiative/
├── app.py
├── Social_Engagement_Analytics_Colab.ipynb
├── requirements.txt
├── README.md
├── data/
├── models/
├── outputs/
└── src/
```
