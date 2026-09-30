# Technology Stack

| Field         | Details                                                   |
| ------------- | --------------------------------------------------------- |
| Project Title | LegalEase AI: AI-Powered Legal Document Generator         |
| Team ID       | SWTID-2026-5104                                           |
| Team Size     | 5                                                         |
| Team Leader   | Priyadharsini L                                           |
| Team Members  | Deepa Dharshini D, Naveen Kumar, Tamilselvan, Vinothini P |

---

## Technical Architecture Components

| S.No | Component           | Description                                     | Technology                      |
| ---- | ------------------- | ----------------------------------------------- | ------------------------------- |
| 1    | User Interface      | Web interface for forms, preview and download   | React.js, HTML, CSS, JavaScript |
| 2    | Application Logic-1 | Authentication and user management              | Node.js, Express.js, JWT        |
| 3    | Application Logic-2 | Prompt building and document generation service | Node.js, prompt templates       |
| 4    | Application Logic-3 | PDF / DOCX export                               | jsPDF, docx library             |
| 5    | Generative AI Model | Legal text generation                           | Google Gemini API               |
| 6    | Database            | Users and generated documents                   | MongoDB                         |
| 7    | Cloud Database      | Hosted database                                 | MongoDB Atlas                   |
| 8    | File Storage        | Temporary export files                          | Local file system               |
| 9    | Infrastructure      | Application hosting                             | Render / Vercel (cloud)         |

## Application Characteristics

| S.No | Characteristic           | Description                                         | Technology             |
| ---- | ------------------------ | --------------------------------------------------- | ---------------------- |
| 1    | Open-Source Frameworks   | React, Express, Mongoose                            | React.js, Express.js   |
| 2    | Security Implementations | Password hashing, JWT, HTTPS, environment variables | bcrypt, JWT, dotenv    |
| 3    | Scalable Architecture    | Stateless REST API, cloud database                  | Node.js, MongoDB Atlas |
| 4    | Availability             | Cloud hosting with auto restart                     | Render / Vercel        |
| 5    | Performance              | Caching of templates, optimised prompts             | In-memory cache        |
