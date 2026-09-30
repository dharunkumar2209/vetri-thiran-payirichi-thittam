# Solution Requirements

| Field         | Details                                                   |
| ------------- | --------------------------------------------------------- |
| Project Title | LegalEase AI: AI-Powered Legal Document Generator         |
| Team ID       | SWTID-2026-5104                                           |
| Team Size     | 5                                                         |
| Team Leader   | Priyadharsini L                                           |
| Team Members  | Deepa Dharshini D, Naveen Kumar, Tamilselvan, Vinothini P |

---

## Functional Requirements

| FR No. | Functional Requirement (Epic) | Sub Requirement (Story / Sub-Task)                                             |
| ------ | ----------------------------- | ------------------------------------------------------------------------------ |
| FR-1   | User Registration             | Registration using email and password; confirmation of successful registration |
| FR-2   | User Login                    | Login with email and password; JWT-based session                               |
| FR-3   | Document Type Selection       | Choose from NDA, Rental Agreement, Service Agreement, Offer Letter             |
| FR-4   | Guided Input Form             | Dynamic form fields based on document type; input validation                   |
| FR-5   | AI Document Generation        | Generate full legal document using LLM from user inputs                        |
| FR-6   | Preview and Edit              | Live preview; edit generated text before download                              |
| FR-7   | Export Document               | Download as PDF and DOCX                                                       |
| FR-8   | Document History              | Save, view, reopen and delete previously generated documents                   |
| FR-9   | Clause Explanation            | Plain-language explanation of selected clauses                                 |
| FR-10  | Legal Disclaimer              | Display a disclaimer that output is not a substitute for a licensed lawyer     |

## Non-Functional Requirements

| NFR No. | Non-Functional Requirement | Description                                                                          |
| ------- | -------------------------- | ------------------------------------------------------------------------------------ |
| NFR-1   | Usability                  | Clean, simple interface usable by non-technical users on desktop and mobile          |
| NFR-2   | Security                   | Password hashing, JWT authentication, HTTPS, API keys kept in environment variables  |
| NFR-3   | Reliability                | Graceful error handling; retry when the AI service fails                             |
| NFR-4   | Performance                | Document generated within 15 seconds; page load under 3 seconds                      |
| NFR-5   | Availability               | Application available 99% of the time during demonstration and evaluation            |
| NFR-6   | Scalability                | Stateless backend that supports multiple concurrent users and new document templates |
| NFR-7   | Privacy                    | User documents visible only to the owner; no third-party sharing of personal data    |
