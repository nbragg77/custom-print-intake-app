# Custom Print Request App

A Flask-based web application developed as a proof of concept for improving the intake process for custom-printed product requests.

## Business Problem

Custom print requests were originally submitted through unstructured emails. Requests frequently arrived without all of the information needed to obtain supplier quotes, resulting in multiple rounds of follow-up between the sales representative and the Custom Print team.

The goal of this prototype was to move information gathering upstream by giving sales representatives a structured intake form that captured key requirements at the beginning of the process.

## Solution

The application provides a web-based form for submitting custom product requests. It captures information including:

* Sales representative and customer
* Requested item
* Monthly usage
* Target cost
* Preferred supplier
* Logo/artwork availability
* Desired logo placement
* Order type
* Additional request details

When artwork is available, users can upload supported vector or PDF files directly with the request.

After submission, the Flask application formats the information into a standardized request and automatically emails it to the designated recipient, including the uploaded artwork as an attachment when applicable.

## Workflow

**Sales Rep → Structured Web Form → Validation & Artwork Upload → Automated Email → Custom Print Team**

This replaced an unstructured email-based starting point with a standardized intake process designed to reduce clarification emails and incomplete supplier quote requests.

## Technology

* **Python**
* **Flask**
* **HTML**
* **JavaScript**
* **SMTP / Microsoft 365**
* **Render**
* **GitHub**

## Key Features

* Required fields for critical request information
* Conditional artwork upload based on logo availability
* File-type validation for `.ai`, `.eps`, `.pdf`, and `.svg` artwork
* Automated email generation
* Artwork attachment handling
* Environment variables for credentials and configuration
* Render-compatible deployment

## Project Context

This application was developed as an early functional prototype within a larger custom-print process improvement initiative.

The prototype demonstrated how structured digital intake could reduce administrative back-and-forth and improve the completeness of requests before they reached the Custom Print team.

The broader process redesign extended beyond the application itself and included workflow standardization, request tracking, supplier communication, and clearer ownership throughout the custom-print request lifecycle.

## Security

Credentials and environment-specific configuration are excluded from this repository. Sensitive values are managed through environment variables and are not stored in the source code.
