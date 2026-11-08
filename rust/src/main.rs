//! Save to run clippy. Inlay hints show the types `rust-analyzer` infers.

fn word_lengths(text: &str) -> Vec<(&str, usize)> {
    text.split_whitespace().map(|w| (w, w.len())).collect()
}

fn main() {
    let text = "the quick brown fox";
    for (word, len) in word_lengths(text) {
        println!("{word}: {len}");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn counts_words() {
        assert_eq!(word_lengths("a bb").len(), 2);
    }
}
