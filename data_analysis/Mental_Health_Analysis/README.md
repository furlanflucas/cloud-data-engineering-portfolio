# Analyzing Students' Mental Health

## Project Overview
This project analyzes a dataset containing information about students' mental health, focusing on key metrics such as depression, stress, and social connectedness. By examining these aspects, the project aims to uncover patterns and insights that could help in understanding the factors impacting students' mental well-being.

## Dataset Description
The dataset includes the following key columns:
- **inter_dom**: Indicates whether the student is international or domestic.
- **region**: Geographical region of the student.
- **gender**: Gender of the student.
- **academic**: Academic level (e.g., graduate, undergraduate).
- **age**: Age of the student.
- **stay**: Duration of stay.
- **todep**: Score related to depression levels.
- **tosc**: Score related to social connectedness.
- **toas**: Total adjustment score.

### Preview of the Data
| inter_dom | region | gender | academic | age  | stay | todep | tosc | toas |
|-----------|--------|--------|----------|------|------|-------|------|------|
| Inter     | SEA    | Male   | Grad     | 24.0 | 5.0  | 0.0   | 34.0 | 91.0 |
| Inter     | SEA    | Male   | Grad     | 28.0 | 1.0  | 2.0   | 48.0 | 39.0 |
| Inter     | SEA    | Male   | Grad     | 25.0 | 6.0  | 2.0   | 41.0 | 51.0 |

**Note:** The dataset includes other columns related to family and social relationships, professional support, and additional health metrics.

## Objectives
- To analyze and visualize trends in mental health data across various demographics.
- To identify correlations between different factors and mental health metrics.
- To provide actionable insights that can contribute to supporting students' mental health.

## Key Insights
1. The average depression, social connectedness, and adjustment scores are calculated and compared across different groups (e.g., international vs. domestic students).
2. Data visualizations highlight relationships between demographic factors (e.g., age, region) and mental health metrics.
3. The project explores the impact of support systems (family, friends, professionals) on mental well-being.

## Tools and Libraries
- **Programming Language**: Python
- **Libraries**: 
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
- **Visualization**: Graphs and plots to display key trends and correlations.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/<your_username>/Portfolio.git
   ```
2. Navigate to the project directory and open the Jupyter Notebook:
   ```bash
   cd Portfolio
   jupyter notebook "Analyzing Students' Mental Health.ipynb"
   ```
3. Ensure the dataset `students.csv` is in the same directory as the notebook.

## Future Improvements
- Expand analysis to include predictive modeling for mental health scores.
- Incorporate more datasets to generalize insights.
- Create an interactive dashboard for real-time data visualization.
