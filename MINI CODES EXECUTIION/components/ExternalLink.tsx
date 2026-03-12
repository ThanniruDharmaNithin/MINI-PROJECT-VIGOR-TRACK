import { openBrowserAsync } from 'expo-web-browser';
import React from 'react'; // Import React to support JSX
import { TouchableOpacity, Text, Platform } from 'react-native'; // Ensure that TouchableOpacity, Text, and Platform are imported from react-native

type Props = { href: string; children: React.ReactNode };

export function ExternalLink({ href, children }: Props) {
  return (
    <TouchableOpacity
      onPress={async () => {
        if (Platform.OS !== 'web') {
          await openBrowserAsync(href);
        }
      }}
    >
      <Text>{children}</Text>
    </TouchableOpacity>
  );
}
