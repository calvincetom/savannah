# Backend Technical Challenge

## Project Overview

This project is a simple backend service that implements a customer and orders management system. It includes:
- A REST API to manage customers and orders.
- Authentication and authorization using OpenID Connect.
- SMS notifications sent to customers when an order is added using Africa's Talking SMS gateway.

The project is designed to demonstrate proficiency in backend development, API design, authentication, and automated testing with continuous integration and deployment (CI/CD).

## Technologies Used
- **Python**: The main programming language for the service.
- **Django**: Web framework used for building the service.
- **Django REST Framework (DRF)**: To create REST APIs.
- **PostgreSQL**: The database for storing customer and order data.
- **Africa's Talking**: SMS gateway used for sending notifications.
- **OpenID Connect**: Used for implementing authentication and authorization.
- **Docker**: For containerization of the application.
- **Kubernetes**: Container orchestration platform (optional, for deployment).
- **Ansible**: Configuration management tool (optional, for deployment).
- **CI/CD**: Automated testing and deployment.

## Features

1. **Customer and Order Management**:
   - Customers have basic information: `name` and `code`.
   - Orders include details such as `item`, `amount`, and `time`.

2. **Authentication and Authorization**:
   - OpenID Connect is used for securing the API.

3. **SMS Notification**:
   - When a new order is added, an SMS notification is sent to the customer via Africa’s Talking SMS gateway.

4. **Unit Testing and Coverage**:
   - The service includes automated unit tests with coverage checking.

5. **CI/CD Pipeline**:
   - Automated Continuous Integration (CI) and Continuous Deployment (CD) pipelines are set up. Tests run on every push, and successful builds are automatically deployed.

## Setup and Installation

### Prerequisites

- Python 3.x
- Docker
- PostgreSQL
- Africa’s Talking API credentials
- An OpenID Connect provider (e.g., Google, Auth0)

### Steps

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```

2. **Set up environment variables**:
   Create a `.env` file in the project root with the following information:
   ```env
   DATABASE_URL=postgres://<user>:<password>@localhost:5432/<db_name>
   AFRICAS_TALKING_API_KEY=<your_africas_talking_key>
   AFRICAS_TALKING_USERNAME=<your_africas_talking_username>
   OIDC_CLIENT_ID=<your_oidc_client_id>
   OIDC_CLIENT_SECRET=<your_oidc_client_secret>
   OIDC_ISSUER=<your_oidc_issuer_url>
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the application**:
   ```bash
   python manage.py runserver
   ```

6. **Run the tests**:
   To run the unit tests with coverage:
   ```bash
   coverage run --source='.' manage.py test
   coverage report
   ```

7. **Deploy the application**:
   You can deploy the application to any PaaS/FaaS/IaaS of your choice, such as Heroku, AWS, or Google Cloud. Ensure that the environment variables are configured correctly in your deployment environment.

## API Endpoints

- **Customers API**:
  - `POST /api/v1/customers/`: Create a new customer.
  - `GET /api/v1/customers/`: Retrieve a list of customers.
  - `GET /api/v1/customers/<id>/`: Retrieve details of a specific customer.
  - `PUT /api/v1/customers/<id>/`: Update customer details.
  - `DELETE /api/v1/customers/<id>/`: Delete a customer.

- **Orders API**:
  - `POST /api/v1/orders/`: Create a new order (sends SMS notification to customer).
  - `GET /api/v1/orders/`: Retrieve a list of orders.
  - `GET /api/v1/orders/<id>/`: Retrieve details of a specific order.

## Testing and CI/CD

### Testing
Unit tests have been implemented to cover core functionality, including customer creation, order creation, and SMS notification. Test coverage is monitored using `coverage.py`.

### Continuous Integration (CI)
A CI pipeline is set up to run the tests automatically with each push. The pipeline uses a tool like GitHub Actions, Travis CI, or CircleCI. 

### Continuous Deployment (CD)
The CD pipeline is configured to automatically deploy the service after passing tests.

## SMS Integration

To use Africa's Talking SMS service:
1. Sign up for an account on [Africa's Talking](https://africastalking.com/).
2. Get your API key and username from the Africa’s Talking dashboard.
3. Add these to your `.env` file.

The SMS sending logic is triggered after an order is created, notifying the customer of their new order.

## Database Schema

### Customers
- `name`: String, required
- `code`: String, unique, required

### Orders
- `item`: String, required
- `amount`: Float, required
- `time`: Timestamp, auto-generated

## Security Considerations

- OAuth2/OpenID Connect is used for authentication.
- Proper handling of API tokens and credentials in environment variables.
- Web security best practices implemented (e.g., XSS protection).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or issues, feel free to reach out to the project maintainer at `calvinceotienotom@gmail.com`.