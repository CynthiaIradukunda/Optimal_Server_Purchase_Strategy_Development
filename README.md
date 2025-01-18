## Problem
My case study concerns a communication company that is facing serious internal communication issues. These issues have resulted in missed delivery dates, a loss of market share, and a significant drop in stock value. The problem has been exacerbated by a lack of coordination between the marketing, sales, and manufacturing departments, which has led to production inefficiencies and inventory mismatches, as the company’s executive has presented. 

To solve this problem, company executive Mr. Gofero proposes installing an internal company-wide computer network to enhance communication across departments. The implementation is planned over five months, with a phased approach to connecting different departments per month, saving the first for staff buy-in and education. 

## Data Used
1. Departments and Employees:

- Sales (50), Manufacturing (180), Warehouse (30), Marketing (70).

2. Server Types and Costs:

- Standard Intel Pentium PC: $2,500 (30 employees).

- Enhanced Intel Pentium PC: $5,000 (80 employees).

- SGI Workstation: $10,000 (200 employees, 10% discount in Months 1-2).

- Sun Workstation: $25,000 (2,000 employees, 25% discount in Months 1-2).

## Methodology and Language
1. Modeling Approach:

- Integer Programming (IP) using Python's PuLP library.

- Defined decision variables, objective functions, and constraints.

2. Optimization Goals:

- Minimize monthly server costs while meeting department needs.

- Minimize total cost over five months, leveraging discounts.

3. Constraints:

- Budget and capacity limits.

- Server allocation for increasing employee needs per month.

## Results
### Approach A: Minimize Monthly Costs:

| Month | Server Purchased | Cost |
| ----- | ---------------- | ---- |
| 2 | 2 Standard PCs | $5,000 |
| 3 | 1 SGI Workstation | $10,000|
| 4 |  No purchase | $0 |
| 5 | 1 Enhanced PC | $5,000 |
| Total | - | $20,000 |

Key Insight: Focused on immediate needs, leading to higher overall costs.

### Approach B: Minimize Total Costs:

| Month | Server Purchased | Cost |
| ----- | ---------------- | ---- |
| 1 | 1 | SGI Workstation | $10,000
| 2 | No purchase | $0 |
| 3 | 1 SGI Workstation | $9,000 |
| 4 | No purchase | $0 |
| 5 | No purchase | $0 |
| Total | - | $19,000|

Key Insight: Strategic early purchases optimized costs through discounts.

### Comparison Table:

| Approach | Total Cost | Key Purchases | Discounts Utilized |
| ----- | ------------- | ------------- | ------------------ |
| A | $20,000 | Multiple small servers monthly | Limited |
| B | $19,000 | Early larger servers | Fully leveraged |

## Recommendation

For long-term cost savings and early discounts utilization, I recommend the company to opt for the second Approach (Approach B). Doing this will also help it account for operational costs, training, and potential future growth during implementation.


