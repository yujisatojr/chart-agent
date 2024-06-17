# AI Chart Agent

## Description

This chart agent app helps you generate a simple chart based on the topic of your choice and online data.

![Screenshot1](https://my-aws-assets.s3.us-west-2.amazonaws.com/chart-agent-1.png)

![Screenshot2](https://my-aws-assets.s3.us-west-2.amazonaws.com/chart-agent-2.png)

## Getting Started

To get started on your local machine, follow the steps below:

### Setting Up Your OpenAI API Key

1. Open a terminal and navigate to the `server` directory:

   ```bash
   cd server
   ```

2. Create a new file named `.env` to store your environment variables:

   ```bash
   touch .env
   ```

3. Open the `.env` file in a text editor of your choice, and add the following line, replacing `<your_api_key>` with your actual OpenAI API key:

   ```dotenv
   # .env file
   OPENAI_API_KEY=<your_api_key>
   ```

4. Save the `.env` file and update your terminal session to include the new environment variables:

   ```bash
   source .env
   ```

### Backend (FastAPI)

1. Navigate to the project directory:

   ```bash
   cd server
   ```

2. Create a virtual environment and activate it (MacOS):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server using `uvicorn`:

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 5000 --reload
   ```

### Frontend (React)

1. Navigate to the project directory:

   ```bash
   cd client
   ```

2. Install the required dependencies using `npm`:

   ```bash
   npm install
   ```

3. Run the app in development mode:

   ```bash
   npm start
   ```

4. Open [http://localhost:3000](http://localhost:3000) to view the app in your browser.

The page will reload when you make changes. You may also see any lint errors in the console.