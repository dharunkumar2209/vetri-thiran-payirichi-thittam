# Code-Layout, Readability and Reusability

| Field         | Details                                                   |
| ------------- | --------------------------------------------------------- |
| Project Title | LegalEase AI: AI-Powered Legal Document Generator         |
| Team ID       | SWTID-2026-5104                                           |
| Team Size     | 5                                                         |
| Team Leader   | Priyadharsini L                                           |
| Team Members  | Deepa Dharshini D, Naveen Kumar, Tamilselvan, Vinothini P |

---

## Project Folder Structure

| Folder / File            | Purpose                                                       |
| ------------------------ | ------------------------------------------------------------- |
| `client/src/components/` | Reusable UI components (forms, buttons, preview card)         |
| `client/src/pages/`      | Page-level screens (Login, Select Document, Preview, History) |
| `client/src/services/`   | API calling functions                                         |
| `server/routes/`         | API route definitions                                         |
| `server/controllers/`    | Request handling logic                                        |
| `server/services/`       | Prompt builder, Gemini service, export service                |
| `server/models/`         | MongoDB schemas                                               |
| `server/middleware/`     | Authentication and error-handling middleware                  |
| `server/templates/`      | Legal document templates in JSON                              |
| `.env.example`           | Sample environment variables (no secrets)                     |

## Quality Practices

| S.No | Parameter         | Practice Followed                                                                          |
| ---- | ----------------- | ------------------------------------------------------------------------------------------ |
| 1    | Code Layout       | Separate client and server; MVC structure on backend                                       |
| 2    | Readability       | Meaningful names, consistent indentation, comments on complex logic                        |
| 3    | Reusability       | Shared form component for all document types; templates stored as JSON; common API service |
| 4    | Error Handling    | Central error middleware; user-friendly messages                                           |
| 5    | Security          | Secrets in `.env`; passwords hashed; protected routes                                      |
| 6    | Version Control   | Feature branches, pull requests and review by Team Leader                                  |
| 7    | Naming Convention | camelCase for variables, PascalCase for React components                                   |
