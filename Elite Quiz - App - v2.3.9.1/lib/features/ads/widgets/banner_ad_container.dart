import 'dart:developer';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutterquiz/features/profile_management/cubits/user_details_cubit.dart';
import 'package:flutterquiz/features/system_config/cubits/system_config_cubit.dart';
import 'package:flutterquiz/features/system_config/model/ad_type.dart';
import 'package:flutterquiz/utils/extensions.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';
import 'package:ironsource_mediation/ironsource_mediation.dart';
import 'package:unity_ads_plugin/unity_ads_plugin.dart';

class BannerAdContainer extends StatefulWidget {
  const BannerAdContainer({super.key});

  @override
  State<BannerAdContainer> createState() => _BannerAdContainer();
}

class _BannerAdContainer extends State<BannerAdContainer> {
  BannerAd? _localBannerAd;
  UnityBannerAd? _localUnityBannerAd;
  bool _isAdLoaded = false;
  bool _hasLoadedAd = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (!_hasLoadedAd) {
      _hasLoadedAd = true;
      _loadAd();
    }
  }

  Future<void> _loadAd() async {
    final config = context.read<SystemConfigCubit>();
    final hasRemovedAds = context.read<UserDetailsCubit>().removeAds();
    if (!config.isAdsEnable || hasRemovedAds) return;

    if (config.adsType == AdType.admob) {
      await _loadGoogleBannerAd();
    } else if (config.adsType == AdType.unity) {
      _loadUnityBannerAd();
    } else if (config.adsType == AdType.ironSource) {
      if (config.ironSourceBannerId.isNotEmpty) {
        setState(() => _isAdLoaded = true);
      }
    }
  }

  Future<void> _loadGoogleBannerAd() async {
    final config = context.read<SystemConfigCubit>();
    final size =
        await AdSize.getCurrentOrientationAnchoredAdaptiveBannerAdSize(
          MediaQuery.sizeOf(context).width.truncate(),
        ) ??
        AdSize.banner;

    _localBannerAd = BannerAd(
      request: const AdRequest(),
      adUnitId: config.googleBannerId,
      listener: BannerAdListener(
        onAdLoaded: (ad) {
          if (mounted) {
            setState(() => _isAdLoaded = true);
          }
        },
        onAdFailedToLoad: (Ad ad, LoadAdError error) async {
          log('BannerAd failedToLoad: $error');
          await ad.dispose();
        },
      ),
      size: size,
    );

    await _localBannerAd?.load();
  }

  void _loadUnityBannerAd() {
    final placementName = Platform.isIOS ? 'Banner_iOS' : 'Banner_Android';

    _localUnityBannerAd = UnityBannerAd(
      placementId: placementName,
      onLoad: (_) {
        if (mounted) {
          setState(() => _isAdLoaded = true);
        }
      },
      onFailed: (placementId, error, message) {
        log('Banner Ad $placementId failed: $error $message');
      },
    );
  }

  @override
  void dispose() {
    _localBannerAd?.dispose();
    _localBannerAd = null;
    _localUnityBannerAd = null;
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final config = context.read<SystemConfigCubit>();
    final hasRemovedAds = context.read<UserDetailsCubit>().removeAds();

    if (!config.isAdsEnable || hasRemovedAds || !_isAdLoaded) {
      return const SizedBox.shrink();
    }
    

    if (config.adsType == AdType.admob && _localBannerAd != null) {
      return SizedBox(
        width: _localBannerAd!.size.width.toDouble(),
        height: _localBannerAd!.size.height.toDouble(),
        child: AdWidget(ad: _localBannerAd!),
      );
    } else if (config.adsType == AdType.unity && _localUnityBannerAd != null) {
      return SizedBox(
        height: _localUnityBannerAd!.size.height.toDouble(),
        width: _localUnityBannerAd!.size.width.toDouble(),
        child: _localUnityBannerAd,
      );
    } else if (config.adsType == AdType.ironSource) {
      final adKey = GlobalKey<LevelPlayBannerAdViewState>();
      final adSize = LevelPlayAdSize.BANNER;

      return Padding(
        padding: EdgeInsets.only(bottom: context.padding.bottom),
        child: SizedBox(
          width: adSize.width.toDouble(),
          height: adSize.height.toDouble(),
          child: LevelPlayBannerAdView(
            key: adKey,
            adUnitId: config.ironSourceBannerId,
            adSize: adSize,
            listener: _IronSourceBannerAdListener(),
            onPlatformViewCreated: () async {
              await adKey.currentState?.loadAd();
            },
          ),
        ),
      );
    }

    return const SizedBox.shrink();
  }
}

class _IronSourceBannerAdListener extends LevelPlayBannerAdViewListener {
  @override
  void onAdClicked(LevelPlayAdInfo adInfo) {
    log('onAdClicked $adInfo', name: 'LevelPlay');
  }

  @override
  void onAdCollapsed(LevelPlayAdInfo adInfo) {
    log('onAdCollapsed $adInfo', name: 'LevelPlay');
  }

  @override
  void onAdDisplayFailed(LevelPlayAdInfo adInfo, LevelPlayAdError error) {
    log('onAdDisplayFailed $adInfo', name: 'LevelPlay');
  }

  @override
  void onAdDisplayed(LevelPlayAdInfo adInfo) {
    log('onAdDisplayed $adInfo', name: 'LevelPlay');
  }

  @override
  void onAdExpanded(LevelPlayAdInfo adInfo) {
    log('onAdExpanded $adInfo', name: 'LevelPlay');
  }

  @override
  void onAdLeftApplication(LevelPlayAdInfo adInfo) {
    log('onAdLeftApplication $adInfo', name: 'LevelPlay');
  }

  @override
  void onAdLoadFailed(LevelPlayAdError error) {
    log('onAdLoadFailed $error', name: 'LevelPlay');
  }

  @override
  void onAdLoaded(LevelPlayAdInfo adInfo) {
    log('onAdLoaded $adInfo', name: 'LevelPlay');
  }
}
