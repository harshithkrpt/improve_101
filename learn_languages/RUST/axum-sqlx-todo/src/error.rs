use axum::{http::StatusCode, response::{IntoResponse, Response}, Json};
use serde::Serialize;
use thiserror::Error;


pub enum AppError {
    BadRequest(String),
    NotFound,
    SqlX(sqlx::Error),
    Other(anyhow::Error),
}

struct ErrorBody  {
    error: String
}

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        let (status, msg) = match &self {
            AppError::BadRequest(m) => (StatusCode::BAD_REQUEST, m.to_string()),
            AppError::NotFound => (StatusCode::NOT_FOUND, "Not Found".into()),
            AppError::SqlX(e) => (StatusCode::INTERNAL_SERVER_ERROR, e.to_string()),
            AppError::Other(e) => (StatusCode::INTERNAL_SERVER_ERROR, e.to_string()),
        }
    } 
}