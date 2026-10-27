use day1::parse::parse_file;

fn main() {
    let mut total = 0;
    let values = parse_file("everybody_codes_e2026_q01_p1.txt").unwrap();

    for value in &values{
        total += ((value - 1).isqrt() + 1).pow(2) - value;
    }
    println!("Part 1: {}", total);


    let values = parse_file("everybody_codes_e2026_q01_p2.txt").unwrap();
    total = 0;

    for value in values {
        let side = ((value - 4) as f64 / 4.0).ceil() as i32;
        let mut perimeter = (side + 2) * 2 + ((side) * 2);

        if perimeter < 8 {
            perimeter = 8;
        }
        total += perimeter - value;
    }

    println!("Part 2: {}", total);

    let values = parse_file("everybody_codes_e2026_q01_p3.txt").unwrap();
    total = 0;

    for value in values {
        let mut base = (value + 1).isqrt();

        if base * base < value + 1 {
            base += 1;
        }
        if base % 2 == 0 {
            base += 1;
        }
        if base < 3 {
            base = 3;
        };
        total += base.pow(2) - 1 - value;
    }

    println!("Part 3: {}", total);
}
