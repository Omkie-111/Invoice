# Invoice Management API

This project is a Django REST API for managing invoices and their details. The API allows creating and updating invoices along with multiple associated invoice details in a single request. Built with Django REST Framework, the API includes nested serializers for efficient data handling.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Models](#models)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Features

- **Nested Serialization**: Supports nested serializer to handle multiple invoice details within an invoice request.
- **Single API Call**: Create and update an invoice along with all its details in a single API request.
- **Data Validation**: Ensures valid data for `Invoice` and `InvoiceDetail` models.

## Project Structure

```
.
├── neuro
│   ├── settings.py         # Main Django settings configuration
│   ├── urls.py             # URL configuration for the project
│   ├── wsgi.py             # WSGI entry point for deployment
│   ├── asgi.py             # ASGI entry point for asynchronous support
│   └── __init__.py
├── apis
│   ├── migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py           # Contains the Invoice and InvoiceDetail models
│   ├── serializers.py      # Defines serializers for nested data handling
│   ├── views.py            # Defines the API views
│   └── urls.py             # Routes for the API
├── manage.py
└── README.md
```


## Models

### Invoice Model

| Field           | Type             | Description             |
|-----------------|------------------|-------------------------|
| `id`            | AutoField        | Primary key             |
| `invoice_number`| CharField (unique)| Unique invoice number   |
| `customer_name` | CharField        | Customer's name         |
| `date`          | DateField        | Invoice date            |

### InvoiceDetail Model

| Field           | Type             | Description                |
|-----------------|------------------|----------------------------|
| `id`            | AutoField        | Primary key                |
| `invoice`       | ForeignKey       | References Invoice         |
| `description`   | CharField        | Item description           |
| `quantity`      | IntegerField     | Quantity of item           |
| `price`         | DecimalField     | Price per item             |
| `line_total`    | DecimalField     | Computed total (quantity * price) |

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- Django REST Framework

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Omkie-111/Invoice.git
   cd Invoice
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## Configuration

Update the database and other configurations in the `settings.py` file as needed.

## Usage

### Starting the Application

With the server running, you can access the browsable API at `http://127.0.0.1:8000/api/invoices/`.

### Example Payloads

#### Creating an Invoice
Use the following JSON payload to create an invoice with details:

```json
{
  "invoice_number": "INV001",
  "customer_name": "John Doe",
  "date": "2024-11-12",
  "details": [
    {
      "description": "Product A",
      "quantity": 2,
      "price": 50.00,
      "line_total": 100.00
    },
    {
      "description": "Product B",
      "quantity": 1,
      "price": 75.00,
      "line_total": 75.00
    }
  ]
}
```

#### Updating an Invoice
For updating, use the same endpoint (`PUT /api/invoices/`) with the `invoice_number` of the invoice you wish to update.

## API Endpoints

| Method | Endpoint       | Description             |
|--------|----------------|-------------------------|
| POST   | `/api/invoices/` | Creates a new invoice with details |
| PUT    | `/api/invoices/` | Updates an existing invoice and replaces old details |

### Response Structure

On success, both `POST` and `PUT` requests will return the invoice object, including all associated details.
