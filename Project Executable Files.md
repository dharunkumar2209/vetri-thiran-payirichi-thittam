# Project Executable Files

| Field         | Details                                                   |
| ------------- | --------------------------------------------------------- |
| Project Title | LegalEase AI: AI-Powered Legal Document Generator         |
| Team ID       | SWTID-2026-5104                                           |
| Team Size     | 5                                                         |
| Team Leader   | Priyadharsini L                                           |
| Team Members  | Deepa Dharshini D, Naveen Kumar, Tamilselvan, Vinothini P |

---

## Setup and Run Instructions

| Step | Action                      | Command / Detail                                                                          |
| ---- | --------------------------- | ----------------------------------------------------------------------------------------- |
| 1    | Clone the repository        | `git clone <repository-url>`                                                              |
| 2    | Install server dependencies | `cd server && npm install`                                                                |
| 3    | Install client dependencies | `cd client && npm install`                                                                |
| 4    | Configure environment       | Copy `.env.example` to `.env` and set `MONGO_URI`, `JWT_SECRET`, `GEMINI_API_KEY`, `PORT` |
| 5    | Start backend               | `cd server && npm start`                                                                  |
| 6    | Start frontend              | `cd client && npm start`                                                                  |
| 7    | Open application            | `http://localhost:3000`                                                                   |

## Executable Files

| S.No | File                                           | Purpose                           |
| ---- | ---------------------------------------------- | --------------------------------- |
| 1    | `server/server.js`                             | Backend entry point               |
| 2    | `client/src/index.js`                          | Frontend entry point              |
| 3    | `server/package.json`                          | Backend dependencies and scripts  |
| 4    | `client/package.json`                          | Frontend dependencies and scripts |
| 5    | `.env.example`                                 | Environment variable template     |
| 6    | `postman/LegalEase-AI.postman_collection.json` | API test collection               |

## Environment Variables

| Variable         | Description                     |
| ---------------- | ------------------------------- |
| `PORT`           | Backend port (example: 5000)    |
| `MONGO_URI`      | MongoDB Atlas connection string |
| `JWT_SECRET`     | Secret key for signing tokens   |
| `GEMINI_API_KEY` | Google Gemini API key           |
