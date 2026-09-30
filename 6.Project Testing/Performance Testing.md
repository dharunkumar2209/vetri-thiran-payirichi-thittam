# Performance Testing

| Field         | Details                                                   |
| ------------- | --------------------------------------------------------- |
| Project Title | LegalEase AI: AI-Powered Legal Document Generator         |
| Team ID       | SWTID-2026-5104                                           |
| Team Size     | 5                                                         |
| Team Leader   | Priyadharsini L                                           |
| Team Members  | Deepa Dharshini D, Naveen Kumar, Tamilselvan, Vinothini P |

---

## Functional Test Cases

| Test Case ID | Feature            | Test Scenario                    | Test Steps                             | Expected Result                        | Actual Result         | Status | Tested By         |
| ------------ | ------------------ | -------------------------------- | -------------------------------------- | -------------------------------------- | --------------------- | ------ | ----------------- |
| TC-01        | Registration       | Register with valid details      | Enter name, email, password and submit | Account created, success message shown | Account created       | Pass   | Vinothini P       |
| TC-02        | Registration       | Register with existing email     | Submit an already used email           | Error: email already registered        | Error shown           | Pass   | Vinothini P       |
| TC-03        | Login              | Login with valid credentials     | Enter correct email and password       | Dashboard opens                        | Dashboard opened      | Pass   | Vinothini P       |
| TC-04        | Login              | Login with wrong password        | Enter wrong password                   | Error: invalid credentials             | Error shown           | Pass   | Vinothini P       |
| TC-05        | Document Selection | Choose Rental Agreement          | Click Rental Agreement                 | Rental form is loaded                  | Form loaded           | Pass   | Deepa Dharshini D |
| TC-06        | Input Form         | Submit with empty required field | Leave party name empty and submit      | Validation error displayed             | Error displayed       | Pass   | Deepa Dharshini D |
| TC-07        | AI Generation      | Generate NDA                     | Fill NDA form and click Generate       | Complete NDA generated                 | NDA generated         | Pass   | Tamilselvan       |
| TC-08        | AI Generation      | Gemini API failure               | Use invalid API key                    | Friendly error and retry option        | Error and retry shown | Pass   | Tamilselvan       |
| TC-09        | Edit               | Edit generated text              | Change a clause and save               | Edited text saved                      | Saved                 | Pass   | Deepa Dharshini D |
| TC-10        | Export             | Download as PDF                  | Click Download PDF                     | Formatted PDF downloaded               | PDF downloaded        | Pass   | Vinothini P       |
| TC-11        | Export             | Download as DOCX                 | Click Download DOCX                    | Formatted DOCX downloaded              | DOCX downloaded       | Pass   | Vinothini P       |
| TC-12        | History            | View saved documents             | Open history page                      | List of user's documents shown         | List shown            | Pass   | Naveen Kumar      |
| TC-13        | History            | Access another user's document   | Open another user's document ID        | Access denied                          | Access denied         | Pass   | Naveen Kumar      |
| TC-14        | Clause Explanation | Explain a clause                 | Select a clause and click Explain      | Simple explanation shown               | Explanation shown     | Pass   | Tamilselvan       |

## Performance Testing

| S.No | Parameter                          | Values                                             |
| ---- | ---------------------------------- | -------------------------------------------------- |
| 1    | Page Load Time                     | Under 3 seconds                                    |
| 2    | Document Generation Time (average) | 8 to 12 seconds                                    |
| 3    | Export Time (PDF / DOCX)           | Under 2 seconds                                    |
| 4    | Concurrent Users Tested            | 25 users                                           |
| 5    | API Success Rate                   | 98%                                                |
| 6    | Error Handling                     | All tested error cases show user-friendly messages |
| 7    | Browser Compatibility              | Chrome, Edge, Firefox                              |
| 8    | Device Compatibility               | Desktop and mobile                                 |

## Generative AI Output Quality Evaluation

| S.No | Criteria                | Method                                      | Result                        |
| ---- | ----------------------- | ------------------------------------------- | ----------------------------- |
| 1    | Completeness of clauses | Checked against template clause list        | All mandatory clauses present |
| 2    | Accuracy of user inputs | Verified names, dates and amounts in output | Inputs reflected correctly    |
| 3    | Language clarity        | Team review for plain-language readability  | Clear and readable            |
| 4    | Disclaimer presence     | Checked on every generated document         | Present in all outputs        |

## Test Summary

| Total Test Cases | Passed | Failed | Pass Percentage |
| ---------------- | ------ | ------ | --------------- |
| 14               | 14     | 0      | 100%            |
