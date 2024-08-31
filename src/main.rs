use std::time::Instant;

/* #[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let start = Instant::now();
    let url = "http://localhost:3000";
    let _resp = reqwest::get(url)
        .await?
        .text()
        .await?;
    let duration = start.elapsed();
    let secs = duration.as_secs_f64();
    println!("{}", secs);
    Ok(())
} */
use reqwest::Error;
use tokio::task;
use futures::future::join_all;

async fn fetch(url: &str) -> Result<String, Error> {
    let response = reqwest::get(url).await?;
    let body = response.text().await?;
    Ok(body)
}

#[tokio::main]
async fn main() {
    let start = Instant::now();
    let urls = vec![
        "http://localhost:3000"; 10 // Replace with your desired URLs
    ];

    let mut tasks = Vec::new();

    for url in urls {
        let task = task::spawn(fetch(url));
        tasks.push(task);
    }

    let _results = join_all(tasks).await;

    let duration = start.elapsed();
    let secs = duration.as_secs_f64();
    println!("{}", secs);
}

