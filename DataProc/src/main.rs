fn test_cal_speed() -> i64 {
    let mut amount = 0;
    let time_start = std::time::Instant::now();
    for num in 1..1_000_001 {
        amount += num;
    }
    let time_end = std::time::Instant::now();
    println!("Added 1,000,000 numbers within {:?}", time_end - time_start);
    amount
}

fn main() {
    assert_eq!(test_cal_speed(), 500000500000);
}