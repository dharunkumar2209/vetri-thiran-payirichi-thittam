# Scalability and Future Plan

| Field         | Details                                                   |
| ------------- | --------------------------------------------------------- |
| Project Title | LegalEase AI: AI-Powered Legal Document Generator         |
| Team ID       | SWTID-2026-5104                                           |
| Team Size     | 5                                                         |
| Team Leader   | Priyadharsini L                                           |
| Team Members  | Deepa Dharshini D, Naveen Kumar, Tamilselvan, Vinothini P |

---

## Scalability

| S.No | Area           | Current Design                    | How It Scales                                                                |
| ---- | -------------- | --------------------------------- | ---------------------------------------------------------------------------- |
| 1    | Users          | Stateless REST API with JWT       | Add more server instances behind a load balancer as users grow               |
| 2    | Database       | MongoDB Atlas                     | Upgrade cluster tier, add indexes and sharding for large document volumes    |
| 3    | AI Generation  | Gemini API with prompt templates  | Queue requests, cache common outputs and switch to higher API quota          |
| 4    | Document Types | Templates stored as JSON          | New document types added by adding a template, with no code change           |
| 5    | Export         | PDF and DOCX generated on request | Move export to a background worker for heavy loads                           |
| 6    | Deployment     | Cloud hosting (Render / Vercel)   | Auto-scaling and multi-region deployment                                     |
| 7    | Languages      | English output                    | Add Tamil, Hindi and other languages through prompt and template translation |

## Future Plan

| Phase      | Timeline       | Enhancement                                                            | Benefit                                | Owner             |
| ---------- | -------------- | ---------------------------------------------------------------------- | -------------------------------------- | ----------------- |
| Short Term | 1 to 3 months  | More document types (loan agreement, partnership deed, sale agreement) | Wider coverage for users               | Tamilselvan       |
| Short Term | 1 to 3 months  | Multi-language document generation                                     | Reaches regional users                 | Tamilselvan       |
| Short Term | 1 to 3 months  | Improved UI with mobile-first design                                   | Better experience on phones            | Deepa Dharshini D |
| Mid Term   | 3 to 6 months  | E-signature integration                                                | Documents can be signed online         | Naveen Kumar      |
| Mid Term   | 3 to 6 months  | Email and share document option                                        | Easy sending to other parties          | Naveen Kumar      |
| Mid Term   | 3 to 6 months  | Automated test suite and monitoring                                    | Higher reliability                     | Vinothini P       |
| Long Term  | 6 to 12 months | Lawyer review marketplace                                              | Professional verification of documents | Priyadharsini L   |
| Long Term  | 6 to 12 months | Subscription plans for businesses                                      | Revenue and sustainability             | Priyadharsini L   |
| Long Term  | 6 to 12 months | Mobile application (Android and iOS)                                   | Access anywhere                        | Deepa Dharshini D |
