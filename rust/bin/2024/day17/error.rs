//! Main Crate Error

#[derive(thiserror::Error, Debug)]
pub enum Error {
    #[error("Generic Empty")]
    GE(),

    #[error("Generic {0}")]
    G(String),

    #[error(transparent)]
    IO(#[from] std::io::Error)
}