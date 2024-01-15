#![doc(
    html_logo_url = "https://raw.githubusercontent.com/ADE-Scheduler/ADE-Scheduler/main/static/img/ade_scheduler_icon.png",
    html_favicon_url = "https://raw.githubusercontent.com/ADE-Scheduler/ADE-Scheduler/main/static/img/ade_scheduler_icon.png"
)]
#![doc = include_str!("../README.md")]

pub mod api;
pub mod core;
pub mod error;
pub mod models;
pub mod redis;
pub mod routes;
pub mod schema;
