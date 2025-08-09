class Solution {
public:
    int catMouseGame(vector<vector<int>>& graph) {
        constexpr int DRAW = 0, MOUSE_WIN = 1, CAT_WIN = 2, MOUSE = 0, CAT = 1;
        // mouse postion, cat position, next player, pair(winner, number of move options)

        auto winnerToString = [](int winner) {
            if (winner == 0) return "D"; // Draw
            if (winner == 1) return "M"; // Mouse
            if (winner == 2) return "C"; // Cat
            return "?"; // Unknown
        };

        array<array<array<pair<int, size_t>, 2>, 50>, 50> game;
        // mouse pos, cat pos, next player, win or lose
        queue<array<int, 4>> resolved_states; 
        for (auto c = 1; c < graph.size(); ++c) {
            // if mouse position is 0 then mouse wins.
            // cat position does not matter. # ususally cats turn next
            resolved_states.push({0, c, CAT, game[0][c][CAT].first = MOUSE_WIN});
            // The followig should be unreachable as win 
            // should be happned for mouse in previous step.
            // resolved_states.push({0, c, CAT, game[0][c][MOUSE].first = MOUSE_WIN});
            // cat and mouse in same node. CAT wins regardless of whose turn is next
            resolved_states.push({c, c, CAT, game[c][c][CAT].first = CAT_WIN});
            resolved_states.push({c, c, MOUSE, game[c][c][MOUSE].first = CAT_WIN});
            int options = graph[c].size() - any_of(graph[c].begin(), graph[c].end(), [](int adj){ return adj == 0; });
            for (auto m = 1; m < graph.size(); ++m) {
                game[m][c][MOUSE].second = graph[m].size();
                game[m][c][CAT].second = options;
            }
        }

        while (!resolved_states.empty()) {
            auto [mouse_pos, cat_pos, next_player, result] = resolved_states.front();
            resolved_states.pop();
            // // if (mouse_pos != 0){
            // cout << "Mouse pos: " << mouse_pos << " Cat Pos: " << cat_pos << " Player: " << (next_player == CAT ? "CAT" : "MOUSE") << " Resolved result: " << winnerToString(result) << "\n";
            // // }
            for (const auto& moved_from: next_player == CAT ? graph[mouse_pos]: graph[cat_pos]) {
                auto [prev_mouse_pos, prev_cat_pos, prev_next_player] = next_player == CAT ? tuple(moved_from, cat_pos, MOUSE) : tuple(mouse_pos, moved_from, CAT);
                // MOUSE + 1 = MOUSE_WIN = 1;; CAT + 1 = CAT_WIN = 2 ;; hence prev_next_player + 1 == result 
                // player moved previously is winner in current position thenwe shoudl win. 
                if ((prev_cat_pos != 0)
                    && (game[prev_mouse_pos][prev_cat_pos][prev_next_player].first == DRAW)
                    && ((prev_next_player + 1 == result) || (--game[prev_mouse_pos][prev_cat_pos][prev_next_player].second == 0))) {
                    if ((prev_mouse_pos == 1) && (prev_cat_pos == 2) && (prev_next_player == MOUSE)) return result;
                    resolved_states.push({prev_mouse_pos, prev_cat_pos, prev_next_player, game[prev_mouse_pos][prev_cat_pos][prev_next_player].first = result});
            //         if (prev_mouse_pos != 0){
            // cout << " P Mouse pos: " << prev_mouse_pos << " P Cat Pos: " << prev_cat_pos << " P  Player: " << (prev_next_player == CAT ? "CAT" : "MOUSE") << " P Resolved result: " << winnerToString(result) << "\n";
            //     }
                }
                // if (mouse_pos != 0){
                // this->printGameArray(game, graph.size());
                // }
            }
        }
        return DRAW;
    }
void printGameArray(const array<array<array<pair<int, size_t>, 2>, 50>, 50>& game, size_t N) {
        // Ensure N does not exceed the array bounds
        if (N > 50) {
            cout << "Error: N exceeds array bounds (50). Clamping to 50.\n";
            N = 50;
        }

        // Helper function to map winner to string
        auto winnerToString = [](int winner) {
            if (winner == 0) return "D"; // Draw
            if (winner == 1) return "M"; // Mouse
            if (winner == 2) return "C"; // Cat
            return "?"; // Unknown
        };

        // Print matrix for Mouse's turn (next_player = 0)
        cout << "\nGame State (Next Player: Mouse)\n";
        cout << "M\\C|";
        for (size_t cat = 0; cat < N; ++cat) {
            cout << setw(6) << cat << "|";
        }
        cout << "\n";
        cout << string(4 + N * 7, '-') << "\n";
        for (size_t mouse = 0; mouse < N; ++mouse) {
            cout << mouse << "  |";
            for (size_t cat = 0; cat < N; ++cat) {
                const auto& p = game[mouse][cat][0]; // Mouse's turn
                cout << setw(4) << winnerToString(p.first) << ":" << p.second << "|";
            }
            cout << "\n";
        }

        // Print matrix for Cat's turn (next_player = 1)
        cout << "\nGame State (Next Player: Cat)\n";
        cout << "M\\C|";
        for (size_t cat = 0; cat < N; ++cat) {
            cout << setw(6) << cat << "|";
        }
        cout << "\n";
        cout << string(4 + N * 7, '-') << "\n";
        for (size_t mouse = 0; mouse < N; ++mouse) {
            cout << mouse << "  |";
            for (size_t cat = 0; cat < N; ++cat) {
                const auto& p = game[mouse][cat][1]; // Cat's turn
                cout << setw(4) << winnerToString(p.first) << ":" << p.second << "|";
            }
            cout << "\n";
        }
        cout << "\n";
    }
};