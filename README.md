# 📬 Smart Cold Outreach Companion

**Smart Cold Outreach Companion** is an AI-powered tool designed to streamline your job application process by generating tailored cold emails based on job listings. Simply input the job listing URL, and this tool will analyze job details, match your skills, and produce personalized email drafts with relevant portfolio links!

## Features
- 🧠 **AI-Powered Cold Email Generation**: Generates customized job application emails based on job listing URLs.
- 🎯 **Skill Matching**: Matches job requirements with your skills and portfolio.
- 💼 **Easy-to-Use**: Just enter the job URL and get a ready-to-send cold email.
- 🔗 **Portfolio Integration**: Automatically inserts relevant portfolio links into the email.
- ⚡ **Fast and Efficient**: Get a personalized cold email in seconds, tailored for the specific job you're applying to.
- 🔍 **ChromoDB Integration**: Leverages ChromoDB for efficient data retrieval and management of job listings.
- 🤖 **ChatGroq-Powered Conversations**: Uses ChatGroq for smarter, real-time AI interactions and query processing.

![Architecture Diagram](imgs/architecture.png "Architecture Diagram")


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MdThanish/Smart-Cold-Outreach-Companion.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:
    ```bash
    streamlit run main.py
    ```

## Usage

1. Open the app in your browser.
2. Enter the job listing URL in the input box.
3. Click "Generate Cold Email" and let the tool handle the rest.
4. The app will display a tailored cold email ready to be sent!

## Example

Input a job listing URL, and you'll get something like this:

```markdown
Subject: Application for [Job Title] at [Company Name]

Dear [Hiring Manager's Name],

I came across the [Job Title] role at [Company Name] and was excited to apply. With my experience in [mention relevant skills] and [specific projects or accomplishments], I believe I am a strong fit for the position.

I have attached relevant work from my portfolio, which demonstrates my ability in [skills] that align with your requirements. I would love the opportunity to discuss further how I can contribute to your team.

Thank you for your time and consideration.

Best regards,  
[Your Name]  
[Your Portfolio Link]
```

## Technologies Used

- **Streamlit**: For building the web interface.
- **LangChain**: For job data extraction and cold email generation.
- **ChromoDB**: For fast and scalable job data management.
- **ChatGroq**: For real-time AI-powered interaction and query handling.
- **Python**: Backend logic.

## Contributing

We welcome contributions to make Smart Cold Outreach Companion even better! If you have ideas, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
