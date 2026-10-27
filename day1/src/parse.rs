use std::fs::File;
use csv::ReaderBuilder;

pub fn parse_file(filename: &str) -> anyhow::Result<Vec<i32>> {
    let file = File::open(filename)?;
    let mut reader = ReaderBuilder::new()
        .has_headers(false)
        .from_reader(file);

    let mut values = Vec::new();
    for result in reader.deserialize() {
        let row: Vec<i32> = result?;
        values.extend(row);
    }

    Ok(values)
}