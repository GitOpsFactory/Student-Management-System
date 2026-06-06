# 🎓 Student Management System on Kubernetes

A simple microservices-based Student Management System built using **Python Flask**, **PostgreSQL**, **Docker**, **Kubernetes**, and **GitHub Actions CI/CD**.

## 🚀 Tech Stack

* Python Flask
* PostgreSQL 16
* Docker
* Kubernetes
* NGINX Ingress Controller
* GitHub Actions
* Docker Hub
* Minikube

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── student-service/
│   ├── app.py
│   └── Dockerfile
│
├── course-service/
│   ├── app.py
│   └── Dockerfile
│
├── result-service/
│   ├── app.py
│   └── Dockerfile
│
├── database/
│   └── init.sql
│
├── k8s/
│   ├── postgres.yaml
│   ├── student-service.yaml
│   ├── course-service.yaml
│   ├── result-service.yaml
│   └── ingress.yaml
│
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
             NGINX Ingress
             (192.168.49.2)
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼
 /students       /courses        /results
      │               │               │
      ▼               ▼               ▼
Student API    Course API    Result API
 (Flask)         (Flask)       (Flask)
      │               │               │
      └───────────────┼───────────────┘
                      │
                      ▼
                PostgreSQL
```

---

## 📦 Microservices

### Student Service

* Endpoint: `/students`
* Port: `5001`

Returns:

```json
[
  {
    "id": 1,
    "name": "Ravi"
  },
  {
    "id": 2,
    "name": "Kiran"
  }
]
```

---

### Course Service

* Endpoint: `/courses`
* Port: `5002`

Returns:

```json
[
  {
    "id": 1,
    "course": "Python"
  },
  {
    "id": 2,
    "course": "Kubernetes"
  }
]
```

---

### Result Service

* Endpoint: `/results`
* Port: `5003`

Returns:

```json
[
  {
    "id": 1,
    "marks": 95
  },
  {
    "id": 2,
    "marks": 88
  }
]
```

---

## 🗄️ Database

Database: `school`

Tables:

* students
* courses
* results

Sample Data:

```sql
CREATE TABLE students(
id INT,
name VARCHAR(50)
);

INSERT INTO students VALUES
(1,'Ravi'),
(2,'Kiran');

CREATE TABLE courses(
id INT,
course VARCHAR(50)
);

INSERT INTO courses VALUES
(1,'Python'),
(2,'Kubernetes');

CREATE TABLE results(
id INT,
marks INT
);

INSERT INTO results VALUES
(1,95),
(2,88);
```

---

## 🐳 Build Docker Images

```bash
docker build -t <dockerhub-username>/student:v1 ./student-service
docker build -t <dockerhub-username>/course:v1 ./course-service
docker build -t <dockerhub-username>/result:v1 ./result-service
```

Push Images:

```bash
docker push <dockerhub-username>/student:v1
docker push <dockerhub-username>/course:v1
docker push <dockerhub-username>/result:v1
```

---

## ☸️ Deploy to Kubernetes

```bash
kubectl apply -f k8s/postgres.yaml

kubectl apply -f k8s/student-service.yaml
kubectl apply -f k8s/course-service.yaml
kubectl apply -f k8s/result-service.yaml

kubectl apply -f k8s/ingress.yaml
```

Verify:

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

---

## 🌐 Access Application

Check Ingress IP:

```bash
kubectl get ingress
```

Example:

```text
NAME             CLASS   ADDRESS
school-ingress   nginx   192.168.49.2
```

Access APIs:

```text
http://192.168.49.2/students

http://192.168.49.2/courses

http://192.168.49.2/results
```

---

## 🔍 Internal Kubernetes Testing

Create a temporary curl pod:

```bash
kubectl run curlpod --image=curlimages/curl -it --rm -- sh
```

Test services:

```bash
curl http://student-service/students

curl http://course-service/courses

curl http://result-service/results
```

---

## ⚙️ CI/CD Pipeline

GitHub Actions pipeline automatically:

* Checkout source code
* Docker login
* Build Docker images
* Push images to Docker Hub
* Apply Kubernetes manifests
* Update deployments
* Verify rollout status

Pipeline Flow:

```text
Git Push
    │
    ▼
GitHub Actions
    │
    ├── Checkout
    ├── Docker Login
    ├── Build Images
    ├── Push Images
    ├── kubectl apply
    ├── kubectl set image
    ├── Rollout Status
    └── Deployment Verification
```

---

## 📌 Kubernetes Objects Used

* Deployment
* Service (ClusterIP)
* Ingress
* Pod
* ReplicaSet

---

## 🎯 Features

* Microservices Architecture
* Internal Service Communication using ClusterIP
* NGINX Ingress Routing
* PostgreSQL Backend
* Dockerized Applications
* Kubernetes Deployment
* GitHub Actions CI/CD
* Docker Hub Integration
* Rolling Updates

---

## 📸 Sample Output

```bash
$ curl http://student-service/students

[{"id":1,"name":"Ravi"},{"id":2,"name":"Kiran"}]
```

```bash
$ curl http://course-service/courses

[{"id":1,"course":"Python"},{"id":2,"course":"Kubernetes"}]
```

```bash
$ curl http://result-service/results

[{"id":1,"marks":95},{"id":2,"marks":88}]
```

---

## 👨‍💻 Author

**Basavaraj Kuslapur**

DevOps Engineer

Skills:
AWS | Docker | Kubernetes | Jenkins | GitHub Actions | Terraform | Python | Linux
