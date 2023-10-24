use sysinfo::{CpuExt, System, SystemExt};

fn test_cal_speed() -> i64 {

    let mut total_usage = 0.0;

    let mut amount = 0;
    let mut sys = System::new();    
    
    let time_start = std::time::Instant::now();
    sys.refresh_all();
    for num in 1..100_000_001 {
        amount += num;
    }
    let time_end = std::time::Instant::now();
    sys.refresh_cpu();
    for cpu in sys.cpus() {
         total_usage += cpu.cpu_usage();
    }    
    std::thread::sleep(System::MINIMUM_CPU_UPDATE_INTERVAL);
    let average_usage= total_usage / sys.cpus().len() as f32;
    println!("Added 100,000,000 numbers within {:?}", time_end - time_start);
    println!("CPU Usage: {:.2}%", average_usage);
    amount
}

fn main() {
    assert_eq!(test_cal_speed(), 5000000050000000);
}