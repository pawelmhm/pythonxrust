use std::time::Instant;

#[tokio::main]
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
}
