#!/usr/bin/env python3

import json
import subprocess
import sys

def check_service_status(service_name):
    """systemctl을 사용하여 서비스 상태 확인"""
    try:
        result = subprocess.run(['systemctl', 'is-active', service_name], 
                              capture_output=True, text=True, timeout=5)
        return result.stdout.strip() == 'active'
    except Exception as e:
        print(f"서비스 {service_name} 상태 확인 실패: {e}")
        return False

def check_security_status():
    """보안 상태 점검"""
    try:
        # 설정 파일 로드
        with open('default-log.conf', 'r') as f:
            config = json.load(f)
        
        print("=== HamoniKR 보안 도구 - 시스템 보안 상태 ===\n")
        
        for category, settings in config.items():
            service_name = settings.get('service_name', '')
            is_active = check_service_status(service_name)
            
            status = "✓ 정상" if is_active else "✗ 비활성"
            print(f"{category.upper():15} : {status} ({service_name})")
        
        print("\n=== 추가 보안 점검 ===")
        
        # UFW 방화벽 상태 확인
        try:
            ufw_result = subprocess.run(['ufw', 'status'], capture_output=True, text=True)
            if 'Status: active' in ufw_result.stdout:
                print(f"{'FIREWALL':15} : ✓ UFW 활성화됨")
            else:
                print(f"{'FIREWALL':15} : ✗ UFW 비활성화됨")
        except:
            print(f"{'FIREWALL':15} : ? UFW 상태 확인 불가")
        
        # SSH 서비스 확인
        ssh_active = check_service_status('ssh')
        print(f"{'SSH':15} : {'✓ 활성' if ssh_active else '✗ 비활성'}")
        
        print(f"\n보안 점검이 완료되었습니다.")
        
    except Exception as e:
        print(f"보안 상태 점검 중 오류 발생: {e}")
        return False
    
    return True

if __name__ == "__main__":
    check_security_status()