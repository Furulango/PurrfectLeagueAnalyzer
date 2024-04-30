CREATE TABLE "matches" (
  "gameId" varchar UNIQUE PRIMARY KEY,
  "region" varchar,
  "gameVersion" varchar,
  "gameDuration" integer
);

CREATE TABLE "participants" (
  "gameId" varchar PRIMARY KEY,
  "summoner1_id" varchar,
  "summoner2_id" varchar,
  "summoner3_id" varchar,
  "summoner4_id" varchar,
  "summoner5_id" varchar,
  "summoner6_id" varchar,
  "summoner7_id" varchar,
  "summoner8_id" varchar,
  "summoner9_id" varchar,
  "summoner10_id" varchar
);

CREATE TABLE "players_info" (
  "puuid" varchar UNIQUE PRIMARY KEY,
  "summonerId" varchar,
  "riotIdGameName" varchar,
  "region" varchar
);

CREATE TABLE "matchInfo" (
  "gameId" varchar,
  "puuid" varchar,
  "riotIdGameName" varchar,
  "all_in_pings" integer,
  "assist_me_pings" integer,
  "assists" integer,
  "bait_pings" integer,
  "baron_kills" integer,
  "basic_pings" integer,
  "bounty_level" integer,
  "champ_experience" integer,
  "champ_level" integer,
  "champion_id" integer,
  "champion_name" varchar,
  "champion_transform" integer,
  "command_pings" integer,
  "consumables_purchased" integer,
  "damage_dealt_to_buildings" integer,
  "damage_dealt_to_objectives" integer,
  "damage_dealt_to_turrets" integer,
  "damage_self_mitigated" integer,
  "danger_pings" integer,
  "deaths" integer,
  "detector_wards_placed" integer,
  "double_kills" integer,
  "dragon_kills" integer,
  "eligible_for_progression" boolean,
  "enemy_missing_pings" integer,
  "enemy_vision_pings" integer,
  "first_blood_assist" boolean,
  "first_blood_kill" boolean,
  "first_tower_assist" boolean,
  "first_tower_kill" boolean,
  "game_ended_in_early_surrender" boolean,
  "game_ended_in_surrender" boolean,
  "get_back_pings" integer,
  "gold_earned" integer,
  "gold_spent" integer,
  "hold_pings" integer,
  "individual_position" varchar,
  "inhibitor_kills" integer,
  "inhibitor_takedowns" integer,
  "inhibitors_lost" integer,
  "item0" integer,
  "item1" integer,
  "item2" integer,
  "item3" integer,
  "item4" integer,
  "item5" integer,
  "item6" integer,
  "items_purchased" integer,
  "killing_sprees" integer,
  "kills" integer,
  "lane" varchar,
  "largest_critical_strike" integer,
  "largest_killing_spree" integer,
  "largest_multi_kill" integer,
  "longest_time_spent_living" integer,
  "magic_damage_dealt" integer,
  "magic_damage_dealt_to_champions" integer,
  "magic_damage_taken" integer,
  "need_vision_pings" integer,
  "neutral_minions_killed" integer,
  "nexus_kills" integer,
  "nexus_lost" integer,
  "nexus_takedowns" integer,
  "objectives_stolen" integer,
  "objectives_stolen_assists" integer,
  "on_my_way_pings" integer,
  "penta_kills" integer,
  "physical_damage_dealt" integer,
  "physical_damage_dealt_to_champions" integer,
  "physical_damage_taken" integer,
  "placement" integer,
  "player_augment1" integer,
  "player_augment2" integer,
  "player_augment3" integer,
  "player_augment4" integer,
  "player_subteam_id" integer,
  "profile_icon" integer,
  "push_pings" integer,
  "quadra_kills" integer,
  "riot_id_name" varchar,
  "riot_id_tagline" varchar,
  "role" varchar,
  "sight_wards_bought_in_game" integer,
  "spell1_casts" integer,
  "spell2_casts" integer,
  "spell3_casts" integer,
  "spell4_casts" integer,
  "subteam_placement" integer,
  "summoner1_casts" integer,
  "summoner1_id" integer,
  "summoner2_casts" integer,
  "summoner2_id" integer,
  "summoner_id" varchar,
  "summoner_level" integer,
  "summoner_name" varchar,
  "team_early_surrendered" boolean,
  "team_id" integer,
  "team_position" varchar,
  "time_ccing_others" integer,
  "time_played" integer,
  "total_ally_jungle_minions_killed" integer,
  "total_damage_dealt" integer,
  "total_damage_dealt_to_champions" integer,
  "total_damage_shielded_on_teammates" integer,
  "total_damage_taken" integer,
  "total_enemy_jungle_minions_killed" integer,
  "total_heal" integer,
  "total_heals_on_teammates" integer,
  "total_minions_killed" integer,
  "total_time_cc_dealt" integer,
  "total_time_spent_dead" integer,
  "total_units_healed" integer,
  "triple_kills" integer,
  "true_damage_dealt" integer,
  "true_damage_dealt_to_champions" integer,
  "true_damage_taken" integer,
  "turret_kills" integer,
  "turret_takedowns" integer,
  "turrets_lost" integer,
  "unreal_kills" integer,
  "vision_cleared_pings" integer,
  "vision_score" integer,
  "vision_wards_bought_in_game" integer,
  "wards_killed" integer,
  "wards_placed" integer,
  "win" boolean,
  PRIMARY KEY ("gameId", "puuid")
);

CREATE TABLE "items" (
  "itemId" integer PRIMARY KEY,
  "name" varchar,
  "description" varchar
);

ALTER TABLE "participants" ADD FOREIGN KEY ("gameId") REFERENCES "matches" ("gameId");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("gameId") REFERENCES "matches" ("gameId");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("puuid") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner1_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner2_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner3_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner4_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner5_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner6_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner7_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner8_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner9_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "participants" ADD FOREIGN KEY ("summoner10_id") REFERENCES "players_info" ("puuid");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("item0") REFERENCES "items" ("itemId");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("item1") REFERENCES "items" ("itemId");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("item2") REFERENCES "items" ("itemId");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("item3") REFERENCES "items" ("itemId");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("item4") REFERENCES "items" ("itemId");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("item5") REFERENCES "items" ("itemId");

ALTER TABLE "matchInfo" ADD FOREIGN KEY ("item6") REFERENCES "items" ("itemId");
