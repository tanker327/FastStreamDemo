# FastStreamDemo

A demo project showcasing the use of [FastStream](https://faststream.airt.ai/) with RabbitMQ for building a modular, scalable message-driven application in Python. This project demonstrates how to dynamically configure queues and exchanges, leveraging FastStream's declarative API and Python's dynamic capabilities for a clean, maintainable codebase.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Local Setup](#local-setup)
  - [Docker Compose Setup](#docker-compose-setup)
- [Improvements](#improvements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Dynamic Configuration**: Queues and exchanges are defined in a single JSON file (`messaging_config.json`) and dynamically loaded at runtime.
- **Modular Design**: Code is organized into `orders` and `logs` modules for producers and consumers.
- **IDE Support**: Queue and exchange names are dynamically generated with autocompletion support in modern IDEs (e.g., PyCharm, VS Code).
- **RabbitMQ Integration**: Uses FastStream with RabbitMQ for message passing, configured via Docker Compose.
- **Simplified Usage**: Producers only need to know exchange names, and consumers only need queue names, abstracting binding logic.

## Project Structure

```
FastStreamDemo/
├── app/
│   ├── brokers.py          # RabbitMQ broker configuration
│   ├── utils.py            # Dynamic queue/exchange loading and class generation
│   ├── main.py             # Application entry point
│   ├── orders/
│   │   ├── consumers.py    # Order-related message consumers
│   │   └── publishers.py   # Order-related message producers
│   ├── logs/
│   │   ├── consumers.py    # Log-related message consumers
│   │   └── publishers.py   # Log-related message producers
├── messaging_config.json   # Configuration for queues and exchanges
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore file
└── docker-compose.yml      # Docker Compose configuration for RabbitMQ
```

## Setup Instructions

### Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tanker327/FastStreamDemo.git
   cd FastStreamDemo
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run RabbitMQ**:
   Ensure RabbitMQ is running locally or update `app/brokers.py` with your RabbitMQ URL. Alternatively, use Docker Compose (see below).

5. **Start the Application**:
   ```bash
   faststream run app.main:app
   ```

### Docker Compose Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tanker327/FastStreamDemo.git
   cd FastStreamDemo
   ```

2. **Start RabbitMQ with Docker Compose**:
   ```bash
   docker-compose up -d
   ```
   RabbitMQ will be available at `amqp://guest:guest@localhost:5672/`.
   Access the management UI at http://localhost:15672 (username: guest, password: guest).

3. **Set Up Python Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   faststream run app.main:app
   ```

5. **Stop RabbitMQ**:
   ```bash
   docker-compose down
   ```

## Improvements

This project evolved through several iterations with significant enhancements to improve usability, maintainability, and developer experience. Below are the key improvements made:

### Dynamic Queue and Exchange Generation
- **Initial State**: Queues and exchanges were manually defined in separate Python files (`queues.py`) for each module, leading to repetitive code.
- **Improvement**: Consolidated definitions into `messaging_config.json` and used `utils.py` to dynamically load and generate RabbitQueue and RabbitExchange objects. This eliminated redundancy and centralized configuration.

### IDE Autocompletion Support
- **Initial State**: Hardcoded strings (e.g., "order-create") were used to reference queues and exchanges, prone to typos and lacking IDE support.
- **Improvement**: Implemented dynamic classes (Queues and Exchanges) with `__getattr__` and `__dir__`, enabling IDE autocompletion (e.g., `queues.order_create`, `exchanges.orders`). Errors now provide a list of available options, reducing mistakes.

### Simplified User Interface
- **Initial State**: Consumers and producers required explicit binding details (exchange, routing key), increasing complexity.
- **Improvement**: Abstracted binding logic into `messaging_config.json`. Producers only specify exchange and routing key (e.g., `exchanges.orders`), and consumers only need queue names (e.g., `queues.order_create`), aligning with user-focused design.

### Code Deduplication
- **Initial State**: Multiple queue classes (e.g., Queues, OrdersQueues, LogsQueues) had duplicated logic for attribute access and autocompletion.
- **Improvement**: Introduced a factory function `create_dynamic_class` in `utils.py` to generate all classes dynamically from `exchanges_raw` and `queues_raw`, eliminating repetition and adhering to DRY principles.

### Modular Structure
- **Initial State**: Flat structure with separate `modules/` directory.
- **Improvement**: Consolidated code into an `app/` directory, renaming `app.py` to `main.py` for clarity, aligning with standard Python application layouts.

### Docker Compose Integration
- **Initial State**: No containerized setup; relied on local RabbitMQ.
- **Improvement**: Added `docker-compose.yml` to start RabbitMQ automatically, updating `brokers.py` to connect to `rabbitmq:5672` within the Docker network. This simplifies setup and ensures consistency across environments.

### Project Generation Script
- **Initial State**: Manual file creation.
- **Improvement**: Created `generate_project.sh`, kept external to the project, to automate directory and file generation, including configuration files like `requirements.txt` and `.gitignore`.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request on GitHub.

### Potential areas for improvement:
- Add environment variable support for configuration.
- Implement a Dockerfile for containerizing the application.
- Extend `messaging_config.json` with advanced RabbitMQ features (e.g., dead-letter queues).

## License

This project is licensed under the MIT License. See the LICENSE file for details (to be added).

