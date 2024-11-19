# Lazy Reloaded Project Documentation

## Overview
Lazy Reloaded is a project designed to enhance user experience and efficiency in handling flat and property management operations. It consists of multiple Django apps, allowing seamless management of data related to landlords, properties, renters, and their interactions.

## Project Structure
Here is a brief overview of the key components of the Lazy Reloaded project:

- **lazyreload/apps/job_applications/**: Manages job-related functionalities such as job applications and company information. Key files include:
  - `models.py`: Defines data models for job applications and companies, including fields for company ID, job title, and application status. Interacts with views to provide data operations.
  - `views.py`: Contains CRUD views for interacting with job applications and companies. Uses serializers to validate data and interacts with models for data management.
  - `migrations/`: Tracks database changes for the job application models to ensure schema consistency.

- **lazyreload/apps/job_applications/**: Manages job-related functionalities such as job applications and company information. Key files include:
  - `models.py`: Defines the data models for job applications and company details.
  - `views.py`: Contains views for interacting with job applications.
  - `migrations/`: Tracks database changes for the job application models.

- **lazyreload/apps/flat_applications/**: Contains logic for managing flats, landlords, and renters. Key files include:
  - `models.py`: Defines data models for landlords, flats, and renters, including relationships between renters and properties. Interacts with views to provide database operations.
  - `views.py`: Contains views for CRUD operations related to properties, landlords, and renters. Uses the models to serve and modify data.
  - `migrations/`: Handles database schema changes for flats, landlords, and renters.

  - `models.py`: Defines the data models for landlords, flats, and renters.
  - `views.py`: Contains views for interacting with the flat data.
  - `migrations/`: Tracks the database changes.

- **lazyreload/apps/core/**: Core utilities and helper functions used across the entire project.
  - `utils.py`: Common utility functions used across different parts of the application, such as data formatting and date-time handling.
  - `admin.py`: Configures the Django admin interface for managing core models, making it easier to handle data in the backend.

  - `utils.py`: Common utility functions.
  - `admin.py`: Django admin interface configurations for core models.

- **myvenv/**: Contains the virtual environment setup for the project, with necessary dependencies and wheels required for development.

- **.github/workflows/**: Configuration for CI/CD pipelines for testing and deploying the project.

## Setting Up the Project
To set up the Lazy Reloaded project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/lazy_reloaded.git
   cd lazy_reloaded
   ```

2. **Create a Virtual Environment**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```

3. **Install Requirements**
   Install the necessary Python packages.
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   Set up the database by running the migrations.
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   Start the Django development server.
   ```bash
   python manage.py runserver
   ```

## Key Functionalities
1. **Job Applications Management**
   - Manage job applications, company profiles, and application statuses using the `job_applications` app.
   - `views.py` provides CRUD operations, while `models.py` defines the schema for the job applications and companies.

2. **Flat and Landlord Management**
   - Add and manage properties, landlords, and renters through the `flat_applications` app.
   - Models define the relationships, while views handle CRUD operations.

3. **Core Utilities**
   - Utility functions in `core/utils.py` provide common support for other apps, ensuring reusability.
   - The admin interface (`admin.py`) facilitates data management through the Django backend portal.

4. **Job Applications Management**
   - Manage job applications, company profiles, and application statuses.
   - CRUD operations for job-related data.

1. **Flat and Landlord Management**
   - Add and manage properties, landlords, and renters.
   - CRUD operations for flats and their associations.

2. **Core Utilities**
   - Utility functions in `core/utils.py` provide support across different parts of the application.
   - Admin interface for managing data through the Django admin portal.

3. **CI/CD Pipeline**
   - GitHub workflows are set up to automate testing and deployment processes to ensure reliability and consistency.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.

Please ensure all changes are properly tested.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

