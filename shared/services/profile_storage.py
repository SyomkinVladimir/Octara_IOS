import json
from shared.profile_parser.vless_parser import parse_vless_url
from shared.models.profile import Profile
import os

class ProfileStorage:
    @staticmethod
    def save(profile: Profile, file_path: str):
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(profile.to_dict(), file, indent=4, ensure_ascii=False)

    @staticmethod
    def load(file_path: str) -> Profile:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return Profile.from_dict(data)
    
    @staticmethod
    def load_many_from_text(text: str) -> list[Profile]:
        profiles = []

        for line in text.splitlines():
            line = line.strip()

            if not line:
                continue

            profile = parse_vless_url(line)
            profiles.append(profile)

        return profiles 
    
    @staticmethod
    def save_many(profiles: list[Profile], file_path: str):
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        data = [profile.to_dict() for profile in profiles]

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False) 

    @staticmethod
    def load_many(file_path: str) -> list[Profile]:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Profile.from_dict(item) for item in data]
    
    @staticmethod
    def find_by_remark(profiles: list[Profile], remark: str):
        for profile in profiles:
            if profile.remark == remark:
                return profile
        return None
    
    @staticmethod
    def replace_by_remark(profiles: list[Profile], updated_profile: Profile) -> bool:
        for index, profile in enumerate(profiles):
            if profile.remark == updated_profile.remark:
                profiles[index] = updated_profile
                return True
        return False
    
    @staticmethod
    def delete_by_remark(profiles: list[Profile], remark: str) -> bool:
        for index, profile in enumerate(profiles):
            if profile.remark == remark:
                del profiles[index]
                return True
        return False