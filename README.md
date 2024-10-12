Project Description :
The Weather Data ETL Pipeline is a robust data integration project designed to extract, transform, and load weather data from the OpenWeatherMap API into a structured format suitable for analysis and reporting. 
This project exemplifies the principles of the ETL (Extract, Transform, Load) process, which is essential for data engineering and analytics. In today's data-driven world, organizations rely on accurate and timely information to make informed decisions. 
The Weather Data ETL Pipeline addresses this need by automating the retrieval of weather data for specific cities, transforming it into a user-friendly format, and storing it in a CSV file for easy access and analysis. 
This project not only demonstrates the technical skills required for ETL development but also highlights the importance of data integration in various applications, such as business intelligence, forecasting, and operational planning.

Key Components
1. Extraction: The pipeline begins by extracting weather data from the OpenWeatherMap API. This involves making HTTP requests to the API endpoint, which returns data in JSON format. The extraction process is designed to handle various cities, allowing users to specify their location of interest.
2. Transformation: Once the data is extracted, it undergoes a transformation process. This step involves parsing the JSON response to extract relevant information, such as the city name, temperature, and weather description. The transformation ensures that the data is clean, consistent, and structured, making it suitable for further analysis.
3. Loading: The final step of the ETL process is loading the transformed data into a CSV file. This format is widely used for data storage and can be easily imported into various data analysis tools and platforms. The pipeline is designed to overwrite the existing CSV file with new data each time it runs, ensuring that users always have access to the most current weather information.

ETL Process
The ETL process in this project follows a systematic approach:
Extract: The pipeline initiates by sending a request to the OpenWeatherMap API, specifying the desired city. The API responds with weather data in JSON format, which is then captured for further processing.
Transform: The extracted JSON data is parsed to isolate key attributes such as:
  - City Name: The name of the city for which the weather data is retrieved.
  - Temperature: The current temperature, which is extracted from the main section of the JSON response.
  - Weather Description: A brief description of the weather conditions, accessed from the weather array in the JSON response.
This transformation step ensures that the data is formatted correctly and is ready for analysis.
Load: After transformation, the data is loaded into a CSV file. This step involves creating a DataFrame using the pandas library and saving it as a CSV file. The pipeline is designed to overwrite the existing file, ensuring that the latest data is always available.

Technical Implementation :
The project is implemented using Python, leveraging libraries such as requests for API interaction, pandas for data manipulation, and dotenv for environment variable management. The use of these libraries enhances the efficiency and readability of the code, making it easier to maintain and extend in the future.

Result :
![image](https://github.com/user-attachments/assets/df482297-a409-4b78-bc99-5574f807484f)
