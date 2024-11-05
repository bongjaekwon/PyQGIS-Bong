# 필요한 모듈 가져오기
from qgis.core import QgsProject, QgsField, QgsFeature
from qgis.PyQt.QtCore import QVariant

# 레이어 불러오기 (기본 활성화된 레이어를 선택할 경우)
layer = iface.activeLayer()

# 속성 테이블에 위도와 경도 필드 추가
provider = layer.dataProvider()
provider.addAttributes([QgsField("latitude", QVariant.Double),
                        QgsField("longitude", QVariant.Double)])
layer.updateFields()

# 각 피처에 대해 중심점 계산 후 위도와 경도 속성에 값 넣기
with edit(layer):
    lat_index = layer.fields().indexOf("latitude")
    lon_index = layer.fields().indexOf("longitude")
    
    for feature in layer.getFeatures():
        # 중심점 좌표 계산
        centroid = feature.geometry().centroid().asPoint()
        
        # 위도와 경도 값 설정
        feature[lat_index] = centroid.y()  # 위도
        feature[lon_index] = centroid.x()  # 경도
        
        # 업데이트
        layer.updateFeature(feature)

# 레이어의 속성 테이블 업데이트
layer.commitChanges()
layer.updateFields()

print("중심 좌표가 속성 테이블에 추가되었습니다.")
