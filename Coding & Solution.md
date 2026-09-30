# Coding & Solution

| Field         | Details                                                   |
| ------------- | --------------------------------------------------------- |
| Project Title | LegalEase AI: AI-Powered Legal Document Generator         |
| Team ID       | SWTID-2026-5104                                           |
| Team Size     | 5                                                         |
| Team Leader   | Priyadharsini L                                           |
| Team Members  | Deepa Dharshini D, Naveen Kumar, Tamilselvan, Vinothini P |

---

## Feature Implementation Summary

| S.No | Feature                     | Module / File                                                   | Technology           | Developer         | Status    |
| ---- | --------------------------- | --------------------------------------------------------------- | -------------------- | ----------------- | --------- |
| 1    | User Registration and Login | `server/routes/auth.js`, `server/controllers/authController.js` | Express, bcrypt, JWT | Naveen Kumar      | Completed |
| 2    | Document Type Selection     | `client/src/pages/SelectDocument.jsx`                           | React                | Deepa Dharshini D | Completed |
| 3    | Dynamic Input Form          | `client/src/components/DocumentForm.jsx`                        | React                | Deepa Dharshini D | Completed |
| 4    | Prompt Builder              | `server/services/promptBuilder.js`                              | Node.js              | Tamilselvan       | Completed |
| 5    | AI Document Generation      | `server/services/geminiService.js`                              | Gemini API           | Tamilselvan       | Completed |
| 6    | Preview and Editor          | `client/src/pages/Preview.jsx`                                  | React                | Deepa Dharshini D | Completed |
| 7    | PDF / DOCX Export           | `server/services/exportService.js`                              | jsPDF, docx          | Vinothini P       | Completed |
| 8    | Document History            | `server/routes/documents.js`, `server/models/Document.js`       | Express, MongoDB     | Naveen Kumar      | Completed |
| 9    | Clause Explanation          | `server/services/clauseExplainer.js`                            | Gemini API           | Tamilselvan       | Completed |
| 10   | Database Design             | `server/models/User.js`, `server/models/Document.js`            | MongoDB, Mongoose    | Priyadharsini L   | Completed |

## API Endpoints

| Method | Endpoint                               | Description                         | Authentication |
| ------ | -------------------------------------- | ----------------------------------- | -------------- |
| POST   | `/api/auth/register`                   | Register a new user                 | No             |
| POST   | `/api/auth/login`                      | Login and receive JWT               | No             |
| GET    | `/api/templates`                       | List document templates             | Yes            |
| POST   | `/api/documents/generate`              | Generate a legal document           | Yes            |
| GET    | `/api/documents`                       | List user's documents               | Yes            |
| GET    | `/api/documents/:id`                   | Get one document                    | Yes            |
| PUT    | `/api/documents/:id`                   | Update edited document              | Yes            |
| DELETE | `/api/documents/:id`                   | Delete a document                   | Yes            |
| GET    | `/api/documents/:id/export?format=pdf` | Export as PDF or DOCX               | Yes            |
| POST   | `/api/documents/explain`               | Explain a clause in simple language | Yes            |

## Sample Prompt Template Used for Generation

| Parameter     | Value                                                                                                             |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| Role          | "You are a legal drafting assistant that writes clear, structured legal documents."                               |
| Inputs        | Document type, party names, dates, amounts, jurisdiction, special clauses                                         |
| Output Format | Title, parties, recitals, numbered clauses, signature block                                                       |
| Safety Rule   | Always add the disclaimer: "This document is AI-generated and is not a substitute for professional legal advice." |
