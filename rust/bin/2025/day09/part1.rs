use log::{debug, info};

type Coord = (i128, i128);

fn main() {
    env_logger::init();

    let content = include_str!("input.txt");

    let coords: Vec<Coord> = content.lines()
        .map(|line| {
            let items: Vec<i128> = line.split(',')
                .map(|val| val.parse::<i128>().unwrap())
                .collect();

            (items[0], items[1])
        }).collect();

    let mut best_area: i128 = 0;
    
    for i in 0..coords.len() {
        for j in (i+1)..coords.len() {
            let (x1, y1) = coords[i];
            let (x2, y2) = coords[j];

            let area = ((x1 - x2).abs() + 1) * ((y1 - y2).abs() + 1);
            best_area = best_area.max(area);
        }
    }

    info!("{:?}", best_area);
}