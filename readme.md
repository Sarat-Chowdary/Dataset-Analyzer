# Dataset Analyzer

An intelligent agentic flow powered by Anthropic's Claude that automatically cleans datasets and answers questions from your data with natural language processing.

## 🚀 Features

- **Automated Data Cleaning**: Intelligently identifies and handles missing values, duplicates, and data inconsistencies
- **Natural Language Querying**: Ask questions about your dataset in plain English
- **Multi-format Support**: Works with CSV, Excel (XLSX/XLS), and other common data formats
- **Interactive Web Interface**: User-friendly Streamlit application for dataset analysis
- **Data Quality Assessment**: Automatic evaluation of data quality with recommendations
- **Export Results**: Save cleaned datasets and analysis results

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Anthropic API key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sarat-Chowdary/Dataset-Analyzer.git
   cd Dataset-Analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```
   # Add your Anthropic API key 
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## 🌐 Getting Started

### Running the Application

```bash
# Start the Streamlit application
streamlit run app.py
```

The application will open in your web browser at `http://localhost:8501`

### Using the Interface

1. **Upload Dataset**: Use the file uploader to select your CSV or Excel file
2. **Data Preview**: View your dataset structure and basic statistics
3. **Ask Questions**: Type natural language questions about your data
4. **Get Insights**: Receive automated analysis and visualizations
5. **Download Results**: Export cleaned datasets and analysis reports

### Example Questions You Can Ask

- "How many unique airlines are in the dataset?"
- "What's the average flight duration by airline?"
- "Show me flights with the highest occupancy rates"
- "Which routes have the most delays?"
- "Create a summary of missing values in each column"
- "Generate a visualization of passenger trends"

## 📁 Project Structure

```
Dataset-Analyzer/
├── Cleaner/
│   ├── data_cleaner.py          # Data cleaning functionality
│   └── helper.py                # Cleaning helper functions
├── llm/
│   ├── chat_agent.py            # Chat interface agent
│   └── data_analyst_agent.py    # Data analysis agent
├── tools/
│   └── tools.py                 # Analysis tools and utilities
├── tests/
│   └── process_rows.py          # Testing utilities
├── uploads/                     # Uploaded dataset storage
│   └── uploaded_data.csv        # Sample uploaded data
├── main.py                      # Streamlit application entry point
├── requirements.txt             # Python dependencies
├── AirlineIDMapping.csv         # Sample dataset
└── .gitignore                   # Git ignore rules
```

## 🧪 Examples

### Flight Data Analysis
Upload your flight dataset through the web interface and ask questions like:
- "Which airline has the most flights?"
- "What's the busiest route?"
- "Show me delay patterns by time of day"

### E-commerce Data
Upload your sales data and get insights with questions such as:
- "What are the top-selling products?"
- "Show me seasonal sales trends"
- "Which customers have the highest lifetime value?"

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.