# Product Workflow Management System

[](https://www.google.com/search?q=https://github.com/your-username/repo)
[](https://opensource.org/licenses/MIT)
[](https://docs.djangoproject.com/)

An enterprise-grade digital transformation platform designed to streamline product lifecycles, automated workflows, and secure data management. Built with a "Shift-Left" security mindset and a systematic UI/UX approach.

## Core Features

  * **Secure Authentication:** Multi-layered auth using JWT and Google OAuth2 (via Django Allauth).
  * **Automated Workflows:** Logic for product tracking from procurement to dispatch.
  * **M-Pesa Integration:** Seamless payment processing using the Daraja API.
  * **Media Management:** Secure image handling and optimization via Cloudinary.
  * **Interactive Documentation:** Real-time API testing through Swagger (OpenAPI 3.0).

-----

## 🛠 Tech Stack

| Category | Technology |
| :--- | :--- |
| **Frontend** | React, Tailwind CSS, shadcn/ui, Vite |
| **Backend** | Django, Django REST Framework (DRF) |
| **Database** | PostgreSQL, Redis (Caching) |
| **DevSecOps** | Docker, Terraform, Trivy (Scanning), GitHub Actions |
| **Infrastructure** | Vercel (Frontend), Render (Backend), Cloudinary |

-----

## ⚙️ Getting Started

### Prerequisites

  * Python 3.10+
  * Node.js 18+
  * Docker & Docker Compose (optional but recommended)

### Local Development Setup

1.  **Clone the repository**

    ```bash
    git clone https://github.com/your-username/product-workflow.git
    cd product-workflow
    ```

2.  **Backend Setup**

    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

3.  **Frontend Setup**

    ```bash
    cd ../frontend
    npm install
    npm run dev
    ```

4.  **Environment Variables**
    Create a `.env` file in both the `/backend` and `/frontend` directories. Refer to `.env.example` for required keys (SECRET\_KEY, CLOUDINARY\_URL, etc.).

-----

## 🔌 API Documentation

This project uses **drf-spectacular** to provide comprehensive OpenAPI 3.0 documentation. Once the server is running locally, you can access the interactive UI at:

  * **Swagger UI:** `http://localhost:8000/api/docs/`
  * **Redoc:** `http://localhost:8000/api/redoc/`

-----

## 🛡 Security & Compliance

We follow a **DevSecOps** approach to ensure data integrity:

  * **Dependency Scanning:** Automated vulnerability checks using Trivy.
  * **CORS Policy:** Strict origin-based access control (configured for Vercel/Render).
  * **Encryption:** Sensitive fields (like M-Pesa keys) are encrypted using the `cryptography` library.

-----

## 🤝 Contributing

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

-----

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Contact

**Joseph Kwanusu** - Lead Architect  
Project Link: [https://github.com/your-username/product-workflow](https://www.google.com/search?q=https://github.com/your-username/product-workflow)

