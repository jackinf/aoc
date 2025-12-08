use std::collections::{HashMap, VecDeque};

type Coord = (u64, u64, u64);

const CHECKS: usize = 10;

fn main() {
    env_logger::init();

    let contents = include_str!("sample0.txt");

    let lines: Vec<Vec<u64>> = contents.lines()
        .map(|line| line.split(',')
            .map(|val| val.trim().parse::<u64>().unwrap())
            .collect()
        )
        .collect();

    let mut distances:  Vec<(Coord, Coord, u64)> = vec![];
    
    for i in 0..lines.len() {
        for j in (i+1)..lines.len() {
            let p1 = (lines[i][0], lines[i][1], lines[i][2]);
            let p2 = (lines[j][0], lines[j][1], lines[j][2]);

            let dx = p1.0.abs_diff(p2.0);
            let dy = p1.1.abs_diff(p2.1);
            let dz = p1.2.abs_diff(p2.2);
            
            let distance = dx * dx + dy * dy + dz * dz;

            distances.push((p1, p2, distance));
        }
    }

    distances.sort_by_key(|&(_, _, dist)| dist);
    let mut distances: VecDeque<(Coord, Coord, u64)> = distances.into_iter().collect();
    let mut circuit_map: HashMap<Coord, u64> = HashMap::new();
    let mut circuit_map_joins: HashMap<u64, u64> = HashMap::new();
    let mut circuit_counter = 1;

    // Helper to find root circuit (follows join chain)
    let find_root = |joins: &HashMap<u64, u64>, circuit: u64| -> u64 {
        let mut current = circuit;
        while let Some(&next) = joins.get(&current) {
            current = next;
        }
        current
    };

    for _ in 0..CHECKS {
        let (p1, p2, _) = distances.pop_front().unwrap();

        let c1_res = circuit_map.get(&p1);
        let c2_res = circuit_map.get(&p2);
        
        match (c1_res, c2_res) {
            (Some(c1), Some(c2)) => {
                // Find roots to avoid creating cycles
                let root1 = find_root(&circuit_map_joins, *c1);
                let root2 = find_root(&circuit_map_joins, *c2);
                if root1 != root2 {
                    circuit_map_joins.insert(root1, root2);
                }
            },
            (Some(c1), None) => {
                circuit_map.insert(p2, *c1);

            },
            (None, Some(c2)) => {
                circuit_map.insert(p1, *c2);
            },
            (None, None) => {
                circuit_map.insert(p1, circuit_counter);
                circuit_map.insert(p2, circuit_counter);
                circuit_counter += 1;
            },
        }
    }

    // Group coordinates by their resolved circuit ID
    let mut final_groups: HashMap<u64, Vec<Coord>> = HashMap::new();
    for (coord, circuit) in &circuit_map {
        let root = find_root(&circuit_map_joins, *circuit);
        final_groups.entry(root).or_insert_with(Vec::new).push(*coord);
    }

    dbg!(&final_groups);
}